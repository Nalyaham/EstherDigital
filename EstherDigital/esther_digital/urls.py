from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products_list, name="product_list"), 
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("contact_us/", views.contact, name="contact_us"),
    path("checkout/<slug:slug>/", views.create_checkout, name="create_checkout"),
    path("order/<uuid:token>/", views.order_status, name="order_status")
]