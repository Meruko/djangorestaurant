# Generated by Django 4.2.6 on 2023-10-22 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("orders", "0002_ordercomposition_alter_order_dishes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="cost",
            field=models.FloatField(default=0.0),
        ),
    ]
