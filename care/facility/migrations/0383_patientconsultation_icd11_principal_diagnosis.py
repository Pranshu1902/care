# Generated by Django 4.2.2 on 2023-09-04 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("facility", "0382_assetservice_remove_asset_last_serviced_on_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="patientconsultation",
            name="icd11_principal_diagnosis",
            field=models.CharField(blank=True, default="", max_length=100, null=True),
        ),
    ]
