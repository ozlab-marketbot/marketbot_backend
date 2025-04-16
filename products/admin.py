from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "external_vendor_code",
        "product_name",
        "sale_price",
        "stock_quantity",
        "category_code",
        "updated_at",
    )
    list_filter = ("category_code", "product_condition", "created_at")
    search_fields = ("external_vendor_code", "product_name")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-updated_at",)

    fieldsets = (
        (None, {
            "fields": (
                "external_vendor_code",
                "product_name",
                "sale_price",
                "stock_quantity",
                "category_code",
                "product_condition",
                "product_description",
                "extra_info",
            ),
        }),
        ("Timestamps", {
            "fields": ("created_at", "updated_at"),
            "classes": ("collapse",),
        }),
    )
