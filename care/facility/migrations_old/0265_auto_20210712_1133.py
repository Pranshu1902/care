# Generated by Django 2.2.11 on 2021-07-12 06:03

import django.contrib.postgres.fields.jsonb
from django.db import migrations

import care.utils.models.validators


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0264_dailyround_in_prone_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dailyround",
            name="bp",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                default=dict,
                validators=[
                    care.utils.models.validators.JSONFieldSchemaValidator(
                        {
                            "$schema": "http://json-schema.org/draft-07/schema#",
                            "additionalProperties": False,
                            "properties": {
                                "diastolic": {"type": "number"},
                                "mean": {"type": "number"},
                                "systolic": {"type": "number"},
                            },
                            "type": "object",
                        }
                    )
                ],
            ),
        ),
    ]
