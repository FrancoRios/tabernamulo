# Generated by Django 3.1.3 on 2020-11-10 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0004_auto_20201110_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingrediente',
            name='Ingrediente2',
        ),
        migrations.RemoveField(
            model_name='ingrediente',
            name='Ingrediente3',
        ),
        migrations.RemoveField(
            model_name='ingrediente',
            name='Ingrediente4',
        ),
        migrations.AlterField(
            model_name='ingrediente',
            name='Preparacion',
            field=models.TextField(),
        ),
    ]