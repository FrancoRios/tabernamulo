# Generated by Django 3.1.3 on 2020-11-10 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0005_auto_20201110_0115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingrediente',
            old_name='Ingrediente1',
            new_name='IngredientePrincipal',
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='IngredienteSecundario',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='IngredienteTerciario',
            field=models.CharField(default=45, max_length=50),
            preserve_default=False,
        ),
    ]