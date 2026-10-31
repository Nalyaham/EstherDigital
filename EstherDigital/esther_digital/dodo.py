from django.conf import settings
from dodopayments import DodoPayments

def create_dodo_product(product):
    client = DodoPayments(
        bearer_token=settings.DODO_PAYMENTS_API_KEY,
        environment=settings.DODO_ENVIRONMENT,
    )

    kwargs = {}
    if product.short_description:
        kwargs["description"] = product.short_description

    dodo_product = client.products.create(
        name=product.title,
        price={
            "type": "one_time_price",
            "currency": product.currency,                      # "USD"
            "price": int((product.price * 100).to_integral_value()),  # cents
        },
        tax_category="e_book",   # confirm this is the right category for you
        metadata={"django_product_id": product.pk},
        **kwargs,
    )

    product.dodo_product_id = dodo_product.product_id
    product.save(update_fields=["dodo_product_id"])
    return dodo_product