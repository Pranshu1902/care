# Generated by Django 2.2.11 on 2022-07-10 08:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0301_auto_20220709_2051"),
        ("users", "0043_auto_20220624_1119"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="home_facility",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="facility.Facility",
            ),
        ),
    ]
