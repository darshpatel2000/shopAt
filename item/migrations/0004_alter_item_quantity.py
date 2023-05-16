# Generated by Django 4.1 on 2023-05-15 18:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("item", "0003_item_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="quantity",
            field=models.IntegerField(
                default=1,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
    ]
