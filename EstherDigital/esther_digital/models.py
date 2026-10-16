from django.db import models
from django.utils.text import slugify

 
class Product(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    description = models.TextField(help_text="Shown on the details page")
    price = models.DecimalField(max_digits=8, decimal_places=2)
    currency = models.CharField(max_length=3, default="USD")
    cover_image = models.ImageField(upload_to="covers/")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ["-created_at"]
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
 
    def __str__(self):
        return self.title


# This class allows one product to have multiple files. 
class ProductFile(models.Model):
    """A bundle has several PDFs, so one product -> many files."""
    product = models.ForeignKey(Product, related_name="files", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)  # e.g. "Emotional Healing Workbook"
    # Store in PRIVATE storage (not public MEDIA) and serve through a view.
    file = models.FileField(upload_to="private_products/")
    position = models.PositiveSmallIntegerField(default=0)
 
    class Meta:
        ordering = ["position"]
 
    def __str__(self):
        return f"{self.product.title} - {self.title}"


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
 
    class Meta:
        ordering = ["-created_at"]
 
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.created_at:%Y-%m-%d}"