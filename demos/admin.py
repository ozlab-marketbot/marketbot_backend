from django.contrib import admin
from .models import (
    Product, ProductImage, ShippingInfo, PromotionInfo,
    Order, OrderItem, Delivery
)

# 🔹 이미지 인라인 (Product 밑에 붙이기)
class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # 추가 행
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.main_image_url:
            return f'<img src="{obj.main_image_url.url}" width="100" />'
        elif obj.sub_image_url:
            return f'<img src="{obj.sub_image_url.url}" width="100" />'
        return "-"
    image_preview.allow_tags = True
    image_preview.short_description = "미리보기"

# 🔹 배송/프로모션도 같이 보여주기
class ShippingInfoInline(admin.StackedInline):
    model = ShippingInfo
    extra = 0

class PromotionInfoInline(admin.StackedInline):
    model = PromotionInfo
    extra = 0

# 🔸 Product 등록
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'sale_price', 'stock_quantity', 'category_code']
    inlines = [ProductImageInline, ShippingInfoInline, PromotionInfoInline]
    search_fields = ['product_name', 'external_vendor_code']
    list_filter = ['category_code']

# 🔸 OrderItem 인라인 (Order 밑에 붙이기)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

# 🔸 Delivery 인라인
class DeliveryInline(admin.StackedInline):
    model = Delivery
    extra = 0

# 🔸 Order 등록
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id', 'order_status', 'order_date', 'receiver_name']
    inlines = [OrderItemInline, DeliveryInline]
    search_fields = ['order_id', 'receiver_name']
    list_filter = ['order_status']

# 🔸 기타 모델 등록
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['product', 'main_image_url', 'sub_image_url']

@admin.register(ShippingInfo)
class ShippingInfoAdmin(admin.ModelAdmin):
    list_display = ['product', 'delivery_info']

@admin.register(PromotionInfo)
class PromotionInfoAdmin(admin.ModelAdmin):
    list_display = ['product', 'promo_info']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'order_product_name', 'order_quantity']

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ['order', 'tracking_number', 'delivery_company']