# Generated by Django 5.0.1 on 2024-04-10 01:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cars", "0003_alter_car_plate"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="car",
            name="created_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="users",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
