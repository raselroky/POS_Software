# Generated by Django 5.0 on 2023-12-27 11:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
        ('purchase', '0001_initial'),
        ('sell', '0002_filter'),
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Quotation',
            fields=[
                ('p_k', models.AutoField(primary_key=True, serialize=False)),
                ('Pay_Term', models.CharField(choices=[('Select', 'Select'), ('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Half of Month', 'Half of Month'), ('Monthly', 'Monthly'), ('Half of Year', 'Half of Year'), ('Yearly', 'Yearly')], default='Select', max_length=1000)),
                ('Sale_Date', models.DateTimeField(blank=True, null=True)),
                ('Billing_Address', models.CharField(blank=True, max_length=1000, null=True)),
                ('Shipping_Address', models.CharField(blank=True, max_length=1000, null=True)),
                ('Invoice_Number', models.CharField(blank=True, max_length=1000, null=True)),
                ('Attach_Document', models.FileField(upload_to='Files/')),
                ('Discount_Type', models.CharField(choices=[('Please Select', 'Please Select'), ('Percentage', 'Percentage'), ('Fixed', 'Fixed')], default='Please Select', max_length=1000)),
                ('Discount_Amount', models.TextField(blank=True, null=True)),
                ('Order_Tax', models.TextField(blank=True, null=True)),
                ('Sell_Note', models.CharField(blank=True, max_length=1000, null=True)),
                ('Shipping_Details', models.CharField(blank=True, max_length=1000, null=True)),
                ('Shipping_Addresss', models.CharField(blank=True, max_length=1000, null=True)),
                ('Shipping_Charges', models.TextField(blank=True, null=True)),
                ('Shipping_Status', models.CharField(choices=[('Select', 'Select'), ('Ordered', 'Ordered'), ('Packed', 'Packed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Select', max_length=1000)),
                ('Shipping_Document', models.FileField(upload_to='Files/')),
                ('Commssion_Agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_management.sales_commission_ager')),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.customers')),
                ('Location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sell.location_set')),
            ],
        ),
    ]