# Generated by Django 4.2.8 on 2024-02-23 06:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("facility", "0414_remove_bed_old_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConsultationClinician",
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
                (
                    "clinician",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "consultation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="facility.patientconsultation",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="patientconsultation",
            name="assigned_clinicians",
            field=models.ManyToManyField(
                related_name="patient_assigned_clinician",
                through="facility.ConsultationClinician",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]