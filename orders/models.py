# demos/models.py

from django.db import models

class Product(models.Model):

    name = models.CharField("상품명", max_length=200)
    brand = models.CharField("브랜드", max_length=100, blank=True)
    model_name = models.CharField("모델명", max_length=100, blank=True)
    manufacturer = models.CharField("제조사", max_length=100, blank=True)
    origin = models.CharField("원산지", max_length=100, blank=True)
    price = models.DecimalField("판매가", max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField("재고 수량", null=True, blank=True)
    description = models.TextField("상품 상세 설명")


class Order(models.Model):
    STATUS_CHOICES = [
        ('READY', '배송대기'),
        ('IN_TRANSIT', '배송중'),
        ('DELIVERED', '배송완료'),
        ('CANCELLED', '취소됨'),
    ]

    order_id = models.CharField(max_length=50)
    platform = models.CharField(max_length=20)
    order_date = models.DateTimeField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    buyer_name = models.CharField(max_length=100)
    receiver_address = models.TextField()
    tracking_number = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.platform} - {self.order_id}"
