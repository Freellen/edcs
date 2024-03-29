# Generated by Django 4.2 on 2024-01-21 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Holiday",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("country", models.CharField(max_length=50)),
                ("local_date", models.DateField()),
                ("name", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ["country", "local_date"],
                "unique_together": {("country", "local_date")},
            },
        ),
    ]
