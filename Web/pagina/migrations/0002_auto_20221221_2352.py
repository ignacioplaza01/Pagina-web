# Generated by Django 3.1 on 2022-12-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='avaluo',
            field=models.IntegerField(max_length=20),
        ),
    ]
