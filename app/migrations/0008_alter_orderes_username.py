# Generated by Django 4.1.7 on 2023-07-03 06:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_remove_orderes_rating_orderes_cancel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderes',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordercus', to=settings.AUTH_USER_MODEL),
        ),
    ]
