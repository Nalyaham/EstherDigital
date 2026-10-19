from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ContactForm
from django.contrib import messages

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

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # saves a ContactMessage row in the database
            messages.success(request, "Thank you! Your message has been sent.")
            return redirect("contact_us")
    else:
        form = ContactForm()
    return render(request, "esther_digital/contact.html", {"form": form})