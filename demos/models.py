from django.db import models

class Product(models.Model):
    name = models.CharField("상품명", max_length=200)
    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    brand = models.CharField("브랜드", max_length=100, blank=True)
    model_name = models.CharField("모델명", max_length=100, blank=True)
    manufacturer = models.CharField("제조사", max_length=100, blank=True)
    origin = models.CharField("원산지", max_length=100, blank=True)
    price = models.DecimalField("판매가", max_digits=12, decimal_places=2)
    stock = models.PositiveIntegerField("재고 수량", null=True, blank=True)  # 선택 사항
    description = models.TextField("상품 상세 설명")