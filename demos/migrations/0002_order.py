# Generated by Django 5.2 on 2025-04-16 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demos', '0001_initial'),
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
    ]
