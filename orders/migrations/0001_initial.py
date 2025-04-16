# Generated by Django 5.1.5 on 2025-04-16 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=50)),
                ('platform', models.CharField(max_length=20)),
                ('order_date', models.DateTimeField()),
                ('status', models.CharField(max_length=30)),
                ('product_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('buyer_name', models.CharField(max_length=100)),
                ('receiver_address', models.TextField()),
                ('tracking_number', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='상품명')),
                ('brand', models.CharField(blank=True, max_length=100, verbose_name='브랜드')),
                ('model_name', models.CharField(blank=True, max_length=100, verbose_name='모델명')),
                ('manufacturer', models.CharField(blank=True, max_length=100, verbose_name='제조사')),
                ('origin', models.CharField(blank=True, max_length=100, verbose_name='원산지')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='판매가')),
                ('stock', models.PositiveIntegerField(blank=True, null=True, verbose_name='재고 수량')),
                ('description', models.TextField(verbose_name='상품 상세 설명')),
            ],
        ),
    ]
