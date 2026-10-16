from django.contrib import admin
from .models import Product, ProductFile, ContactMessage

admin.site.register(Product)
admin.site.register(ProductFile)
admin.site.register(ContactMessage)
