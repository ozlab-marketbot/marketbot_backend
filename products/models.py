from django.db import models

class Product(models.Model):
    # vendor‐agnostic unique code
    external_vendor_code = models.CharField(max_length=100, unique=True)
    # human‐readable name
    product_name         = models.CharField(max_length=255)
    # price in cents (or Decimal for better precision)
    sale_price           = models.DecimalField(max_digits=10, decimal_places=2)
    # how many you have in stock
    stock_quantity       = models.PositiveIntegerField()
    # category identifier
    category_code        = models.CharField(max_length=50, blank=True)
    # detailed description
    product_description  = models.TextField(blank=True)
    # condition (e.g. “new”, “refurbished”)
    product_condition    = models.CharField(max_length=50, blank=True)
    # JSON blob (optional) for extra attributes, options, promotions, etc.
    extra_info           = models.JSONField(default=dict, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_name} ({self.external_vendor_code})"
