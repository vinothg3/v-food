# Generated by Django 4.1.7 on 2023-06-22 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderes',
            name='customer',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='orderes',
            name='product_request',
            field=models.BooleanField(default=True),
        ),
    ]