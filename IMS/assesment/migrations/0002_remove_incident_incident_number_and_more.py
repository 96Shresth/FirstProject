# Generated by Django 4.0.4 on 2022-08-10 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assesment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='incident_number',
        ),
        migrations.AlterField(
            model_name='incident',
            name='reporter_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
