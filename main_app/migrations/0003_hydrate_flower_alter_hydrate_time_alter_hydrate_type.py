# Generated by Django 5.0.1 on 2024-02-06 16:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_hydrate'),
    ]

    operations = [
        migrations.AddField(
            model_name='hydrate',
            name='flower',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main_app.flower'),
        ),
        migrations.AlterField(
            model_name='hydrate',
            name='time',
            field=models.CharField(choices=[('M', 'Morning'), ('N', 'Night')], default=('M', 'Morning'), max_length=2, verbose_name='Hydrate time'),
        ),
        migrations.AlterField(
            model_name='hydrate',
            name='type',
            field=models.CharField(choices=[('SP', 'Spray'), ('SH', 'Shower'), ('SO', 'Soak')], default=('SH', 'Shower'), max_length=2, verbose_name='Hydrate type'),
        ),
    ]