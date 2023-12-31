# Generated by Django 4.2.6 on 2023-10-22 13:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("dishes", "0004_alter_dish_ingridients"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(auto_now=True)),
                (
                    "cost",
                    models.DecimalField(decimal_places=2, default=0.0, max_digits=38),
                ),
                (
                    "dishes",
                    models.ManyToManyField(related_name="dishes", to="dishes.dish"),
                ),
            ],
        ),
    ]
