# Generated by Django 4.2.4 on 2023-08-21 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('comision', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='MyApp.profesor'),
        ),
    ]
