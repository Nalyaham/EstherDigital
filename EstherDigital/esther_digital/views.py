from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Order
from .forms import ContactForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import FileResponse, HttpResponse
from dodopayments import DodoPayments
from django.conf import settings
import os
from django.urls import reverse

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

dodo = DodoPayments(
    bearer_token=settings.DODO_PAYMENTS_API_TEST_KEY,
    environment=settings.DODO_ENVIRONMENT,
)

@require_POST
def create_checkout(request, slug):
    """
    This view takes in the slug of the product and creates and order object of the product,
    then creates a checout session on dodo for the product and gives the session an order id equal to the order token
    """
    product = get_object_or_404(Product, slug=slug, is_active=True)
    if not product.dodo_product_id:
        return HttpResponse("This product isn't set up for checkout yet.", status=400)

    order = Order.objects.create(product=product)
    try:
        session = dodo.checkout_sessions.create(
            product_cart=[{"product_id": product.dodo_product_id, "quantity": 1}],
            return_url=request.build_absolute_uri(reverse("order_status", args=[order.token])),
            metadata={"order_id": str(order.token)},
        )
    except Exception:
        return HttpResponse("Could not start checkout. Please try again.", status=502)

    order.dodo_session_id = session.session_id
    order.save(update_fields=["dodo_session_id"])
    return redirect(session.checkout_url)

def order_status(request, token):
    order = get_object_or_404(Order, token=token)
    return render(request, "esther_digital/order_status.html", {
        "order": order,
        "files": order.product.files.all() if order.status == "paid" else [],
    })