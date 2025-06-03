from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name="Nom de la catégorie")
    cover = models.ImageField(upload_to='Category_covers/', verbose_name="Image de couverture")
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug: # Génère le slug si ce n'est pas déjà fait
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def image_preview(self):
        if self.cover:
            return mark_safe(f'<img src="{self.cover.url}" width="500" height="500" />')
        return "Pas d'image"

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom du produit")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    cover = models.ImageField(upload_to='covers/', verbose_name="Image de couverture")
    description = models.TextField(verbose_name="Description du produit")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Catégorie du produit", default=1,related_name='products')
    tag = models.CharField(max_length=50, blank=True, null=True, verbose_name="Tag du produit", default="new")
    tag_new_added_at = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def image_preview(self):
        if self.cover:
            return mark_safe(f'<img src="{self.cover.url}" width="500" height="500" />')
        return "Pas d'image"

    def save(self, *args, **kwargs):
        # Si le tag est 'New' et que tag_new_added_at n'est pas défini, on le définit maintenant.
        if self.tag and self.tag.lower() == 'new' and not self.tag_new_added_at:
            self.tag_new_added_at = timezone.now()
        # Si le tag n'est PLUS 'New' (c'est-à-dire qu'il est vide/null) mais que tag_new_added_at est défini, on le réinitialise.
        elif (not self.tag or self.tag.lower() != 'new') and self.tag_new_added_at:
            self.tag_new_added_at = None
        super().save(*args, **kwargs)

    def check_and_reset_tag(self, days_limit=30):  # 30 jours par défaut
        if self.tag and self.tag.lower() == 'new' and self.tag_new_added_at:
            if timezone.now() - self.tag_new_added_at > timedelta(days=days_limit):
                self.tag = None
                self.tag_new_added_at = None  # Réinitialise aussi la date
                self.save(update_fields=['tag', 'tag_new_added_at'])  # N'enregistre que ces champs
                return True  # Indique que le tag a été réinitialisé
        return False

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['name']