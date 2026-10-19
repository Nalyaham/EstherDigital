from django.contrib import admin
from .models import Product, ProductFile, ContactMessage, ContactMessage

admin.site.register(ContactMessage)
admin.site.register(Product)
admin.site.register(ProductFile)