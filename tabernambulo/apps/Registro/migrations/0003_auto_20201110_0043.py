# Generated by Django 3.1.3 on 2020-11-10 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0002_auto_20201110_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingrediente',
            old_name='Ingrediente5',
            new_name='Decoracion',
        ),
        migrations.RenameField(
            model_name='ingrediente',
            old_name='Ingrediente6',
            new_name='Preparacion',
        ),
    ]