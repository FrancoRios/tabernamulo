# Generated by Django 3.1.3 on 2020-11-10 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0003_auto_20201110_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='Decoracion',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='Preparacion',
            field=models.CharField(max_length=500),
        ),
    ]