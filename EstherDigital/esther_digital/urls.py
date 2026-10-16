from django.urls import path 
from . import views

url_patterns = [
    path("", views.home, name="home"),
    path("products/", views.products_list, name="product_list"), 
    path("product/<slug:slug>/", views.product_detail, name="product_detail")
]