# Generated by Django 4.1.7 on 2023-06-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_orderes_customer_alter_orderes_product_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderes',
            name='customer',
            field=models.CharField(default='no', max_length=100),
        ),
    ]
