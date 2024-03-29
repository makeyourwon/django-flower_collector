# Generated by Django 5.0.1 on 2024-02-06 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hydrate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Hydrate date')),
                ('time', models.CharField(choices=[('M', 'Morning'), ('N', 'Night')], max_length=2, verbose_name='Hydrate time')),
                ('type', models.CharField(choices=[('SP', 'Spray'), ('SH', 'Shower'), ('SO', 'Soak')], max_length=2, verbose_name='Hydrate type')),
            ],
        ),
    ]
