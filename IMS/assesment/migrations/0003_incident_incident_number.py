# Generated by Django 4.0.4 on 2022-08-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assesment', '0002_remove_incident_incident_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='incident',
            name='incident_number',
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
    ]
