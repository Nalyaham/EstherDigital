from django.shortcuts import render, get_object_or_404
from .models import Product

def home(request):
    products = Product.objects.filter(is_active=True)[:3]
    return render(request, "esther_digital/index.html", {"products": products})

def products_list(request):
    products = Product.objects.filter(is_active=True)
    return render(request, "esther_digital/products.html", {"products": products})

def product_detail(request, slug):
    """details.html: one product, found by its slug."""
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "esther_digital/details.html", {
        "product": product,
        "files": product.files.all(),  # ordered by position
    })
