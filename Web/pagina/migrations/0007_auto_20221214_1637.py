# Generated by Django 3.1 on 2022-12-14 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0006_auto_20221213_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipos',
            name='id',
        ),
        migrations.AlterField(
            model_name='equipos',
            name='codEquipo',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
