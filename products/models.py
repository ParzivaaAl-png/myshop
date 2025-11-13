from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=300, unique=True)
    short_description = models.CharField(max_length=512, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_old = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    in_stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
