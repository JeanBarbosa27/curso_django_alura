# Generated by Django 3.1.4 on 2020-12-07 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receita',
            old_name='mode_preparo',
            new_name='modo_preparo',
        ),
    ]
