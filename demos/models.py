from django.db import models

<<<<<<< Updated upstream
=======
# 상품 모델

>>>>>>> Stashed changes
class Product(models.Model):
    product_name = models.CharField("상품명", max_length=200, null=True, blank=True)
    sale_price = models.PositiveIntegerField("판매가격", null=True, blank=True)
    stock_quantity = models.PositiveIntegerField("재고수량", null=True, blank=True)
    external_vendor_code = models.CharField("외부 상품코드", max_length=100, null=True, blank=True)
    category_code = models.CharField("카테고리 코드", max_length=100, default="UNDEFINED")
    product_description = models.TextField("상품 설명", null=True, blank=True)
    product_condition = models.CharField("상품 상태", max_length=100, null=True, blank=True)
    add_attributes = models.JSONField("부가 속성", null=True, blank=True)
    option_info = models.TextField("옵션 정보", null=True, blank=True)

    def __str__(self):
        return self.product_name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    main_image_url = models.ImageField(upload_to='product_main_images/', null=True, blank=True)
    sub_image_url = models.ImageField(upload_to='product_additional_images/', null=True, blank=True)

class ShippingInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivery_info = models.TextField("배송 정보", null=True, blank=True)

class PromotionInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    promo_info = models.TextField("프로모션 내용", null=True, blank=True)

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('IN_DELIVERY', '배송 중'),
        ('DELIVERED', '배송 완료'),
        ('CANCELLED', '취소됨'),
        ('PENDING', '결제 대기 중'),
        ('PAID', '결제 완료'),
        ('REFUNDED', '환불됨'),
    ]

    order_id = models.CharField("주문번호", max_length=100, unique=True)
    order_date = models.DateTimeField("주문일시")
    order_status = models.CharField("주문 상태", max_length=20, choices=ORDER_STATUS_CHOICES)
    pay_amount = models.DecimalField("결제금액", max_digits=12, decimal_places=2, null=True, blank=True)
    buyer_name = models.CharField("구매자 이름", max_length=100, null=True, blank=True)
    receiver_name = models.CharField("수령자 이름", max_length=100)
    receiver_address = models.CharField("배송지 주소", max_length=255)

    def __str__(self):
        return self.order_id
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    order_product_id = models.CharField("상품별 주문 ID", max_length=100, null=True, blank=True)
    order_product_name = models.CharField("주문 상품명", max_length=200)
    order_quantity = models.PositiveIntegerField("수량")

class Delivery(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    tracking_number = models.CharField("송장번호", max_length=100, null=True, blank=True)
    delivery_company = models.CharField("택배사", max_length=100, null=True, blank=True)
