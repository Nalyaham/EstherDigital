from django.contrib import admin, messages
from .models import Product, ProductFile, ContactMessage, ContactMessage, Order
from .dodo import create_dodo_product

admin.site.register(ContactMessage)
admin.site.register(ProductFile)
admin.site.register(Order)

@admin.action(description="Create product in Dodo Payments")
def push_to_dodo(modeladmin, request, queryset):
    for p in queryset.filter(dodo_product_id=""):   # skips ones already created
        try:
            create_dodo_product(p)
        except Exception as e:
            modeladmin.message_user(request, f"{p.title}: {e}", level=messages.ERROR)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "price", "currency", "dodo_product_id", "is_active")
    actions = [push_to_dodo]



# add to your ProductAdmin:
#     actions = [push_to_dodo]