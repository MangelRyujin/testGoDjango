# Generated by Django 4.2 on 2024-05-04 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('pendiente', 'pendiente'), ('progreso', 'en progreso'), ('completada', 'completada')], default='completada', max_length=10),
        ),
    ]
