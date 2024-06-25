# Generated by Django 5.0.4 on 2024-06-25 09:19

from django.db import migrations
import random


def add_barcode(apps, schema_editor):
    product_model = apps.get_model('main_app', 'Product')
    products = product_model.objects.all()
    barcodes = random.sample(range(100_000_000, 1_000_000_000), len(products))

    for i in range(len(products)):
        product = products[i]
        product.barcode = barcodes[i]
        product.save()


def reverse_add_barcode(apps, schema_editor):
    product_model = apps.get_model('main_app', 'Product')

    for product in product_model.objects.all():
        product.barcode = 0
        product.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_product_barcode'),
    ]

    operations = [
        migrations.RunPython(add_barcode, reverse_add_barcode)
    ]

