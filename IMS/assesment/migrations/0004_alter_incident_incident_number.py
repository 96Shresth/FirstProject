# Generated by Django 4.0.4 on 2022-08-11 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assesment', '0003_incident_incident_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='incident_number',
            field=models.CharField(editable=False, max_length=12, unique=True),
        ),
    ]
