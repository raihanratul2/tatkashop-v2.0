# Generated by Django 4.2.5 on 2023-09-21 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_min_qty_alter_product_pack_size_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='defaults/default.jpg', null=True, upload_to='products/'),
        ),
    ]
