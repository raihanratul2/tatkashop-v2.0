# Generated by Django 4.2.5 on 2023-09-21 16:56

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='brand/')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_slug', autoslug.fields.AutoSlugField(editable=False, populate_from='Product.name', unique=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, default=None, editable=False, null=True, populate_from='name')),
                ('unit', models.CharField(blank=True, choices=[('kg', 'kg'), ('pkt', 'pkt'), ('gm', 'gm'), ('bunch', 'bunch'), ('dozen', 'dozen'), ('liter', 'liter'), ('box', 'box'), ('piece', 'piece')], max_length=100)),
                ('min_qty', models.PositiveIntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[('physical', 'Physical'), ('digital', 'Digital')], default='physical', max_length=10, null=True)),
                ('barcode', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='products1/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products2/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products3/')),
                ('hover_image', models.ImageField(blank=True, null=True, upload_to='products_hover_image/')),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('old_price', models.PositiveIntegerField(blank=True, null=True)),
                ('pack_size', models.CharField(max_length=5, null=True)),
                ('discount', models.CharField(blank=True, choices=[('flat', 'Flat'), ('percent', 'Percent')], max_length=10, null=True)),
                ('tax', models.IntegerField(blank=True, default=5, null=True)),
                ('tax_type', models.CharField(choices=[('flat', 'Flat'), ('percent', 'Percent')], default='percent', max_length=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('qty', models.PositiveIntegerField(blank=True, null=True)),
                ('sku', models.CharField(blank=True, default=None, max_length=30, null=True)),
                ('offer', models.CharField(blank=True, choices=[('today_deal', "Today's Deal"), ('Savings', 'Great Saving'), ('buy1get1', 'Buy 1 Get 1')], default=None, max_length=10, null=True)),
                ('featured', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(blank=True, choices=[('draft', 'Draft'), ('disabled', 'Disabled'), ('published', 'Published')], default='in_review', max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='brand', to='shop.brand')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='shop.category')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='vd', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
