# Generated by Django 4.2.4 on 2023-09-06 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('MyApp', '0003_alumno_apellido_alumno_comision'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='user',
            field=models.OneToOneField(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
