from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name="Nom de la catégorie")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nom du produit")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Prix")
    cover = models.ImageField(upload_to='covers/', verbose_name="Image de couverture")
    description = models.TextField(verbose_name="Description du produit")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name="Catégorie du produit", default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"
        ordering = ['name']