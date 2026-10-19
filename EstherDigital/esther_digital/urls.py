from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.products_list, name="product_list"), 
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("contact_us/", views.contact, name="contact_us")
]