from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Product, Category


def index(request):
    featured_products = Product.objects.all().order_by('-created_at')[:3]
    return  render(request, 'catalog/index.html',{'products':featured_products})

def product_list(request, category=None):
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products, 'category': category})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Les données sont valides
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                f'Message de contact : {subject}',
                f'De: {name} <{email}> \n\n{message}',
                'monmail@oui.com',
                ['egbakoudavid@gmail.com'],
                fail_silently=False,
            )
            # Ajouter un message de succès
            messages.success(request, 'Votre message a été envoyé avec succès !')

            # Rediriger l'utilisateur après l'envoi réussi pour éviter le double-submit
            return redirect('catalog/contact.html') # Créez une URL 'contact_success' ou redirigez vers la même page

        else:
            # Le formulaire n'est pas valide, les erreurs seront affichées automatiquement dans le template
            messages.error(request, 'Veuillez corriger les erreurs dans le formulaire.')
    else:
        form = ContactForm()

    return render(request,'catalog/contact.html',context={'form':form})



def contact_submit(request):
    pass

def products_page(request):
    initial_category_slug = request.GET.get('category', 'all')

    for product in Product.objects.filter(tag__iexact='new'): # Ne vérifie que les produits marqués 'New'
        product.check_and_reset_tag(days_limit=30)

    categories_from_db = Category.objects.all().order_by('name')
    categories = [
        {'id': 'all', 'name': 'All Products', 'slug': 'all'},
        {'id': 'new', 'name': 'New Arrivals', 'slug': 'new'}, # Garde cette entrée si tu utilises un tag 'New'
        *[{'id': category.slug, 'name': category.name, 'slug': category.slug}
          for category in categories_from_db]
    ]


    if initial_category_slug == 'all':
        filtered_products = Product.objects.all()
    elif initial_category_slug == 'new':
        filtered_products = Product.objects.filter(tag__iexact='New')
    else:
        # Recherche la catégorie par son slug
        try:
            category_obj = get_object_or_404(Category, slug__iexact=initial_category_slug)
            filtered_products = Product.objects.filter(category=category_obj)
        except:
            # Si le slug ne correspond à aucune catégorie, affiche tous les produits ou gère l'erreur
            filtered_products = Product.objects.all()
            initial_category_slug = 'all' # Reset active category to 'all' if not found

    filtered_products = filtered_products.order_by('name')

    context = {
        'active_category': initial_category_slug,
        'categories': categories,
        'filtered_products': filtered_products,
    }
    return render(request, 'catalog/product_list.html', context)
