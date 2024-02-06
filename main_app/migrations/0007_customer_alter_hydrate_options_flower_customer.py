# Generated by Django 5.0.1 on 2024-02-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_remove_hydrate_flower_hydrate_flower'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='hydrate',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='flower',
            name='customer',
            field=models.ManyToManyField(to='main_app.customer'),
        ),
    ]