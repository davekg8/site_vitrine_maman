from django.shortcuts import render, get_object_or_404
from .models import Product

def index(request):
    featured_products = Product.objects.all()
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
