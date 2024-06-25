# Generated by Django 5.0.4 on 2024-06-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_product_created_on_product_last_edited_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='No Category', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.CharField(default='No Supplier', max_length=150),
            preserve_default=False,
        ),
    ]
