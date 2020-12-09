# Generated by Django 3.1.4 on 2020-12-07 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0002_auto_20201207_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='pessoa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
