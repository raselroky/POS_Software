# Generated by Django 5.0 on 2023-12-25 19:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('short_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OpeningStock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=255, unique=True)),
                ('location', models.CharField(blank=True, max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('unit_cost_before_tax', models.DecimalField(decimal_places=2, max_digits=10)),
                ('lot_number', models.CharField(blank=True, max_length=255)),
                ('expiry_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=100)),
                ('unit_short_name', models.CharField(blank=True, max_length=100)),
                ('allow_decimal', models.IntegerField(choices=[(0, 'Yes'), (1, 'No')])),
            ],
        ),
        migrations.CreateModel(
            name='Variations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('value', models.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='Warranty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warranty_name', models.CharField(max_length=100)),
                ('warranty_description', models.TextField(blank=True)),
                ('warranty_duration', models.PositiveIntegerField(default=1)),
                ('warranty_duration_type', models.IntegerField(choices=[(0, 'Days'), (1, 'Months'), (2, 'Years')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('category_code', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category')),
            ],
        ),
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=1000)),
                ('sku', models.CharField(max_length=36, unique=True)),
                ('business_locations', models.CharField(max_length=1000)),
                ('alert_quantity', models.PositiveIntegerField()),
                ('manage_stock', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0)),
                ('exc_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('inc_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('margin_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('selling_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.brand')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.subcategory')),
                ('unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.unit')),
                ('variation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.variations')),
                ('warranty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.warranty')),
            ],
        ),
    ]
