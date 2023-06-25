# Generated by Django 2.2.11 on 2020-07-08 12:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0131_auto_20200706_1954"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientsample",
            name="testing_facility",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="facility.Facility",
            ),
        ),
    ]
