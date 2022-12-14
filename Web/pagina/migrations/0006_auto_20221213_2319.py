# Generated by Django 3.1 on 2022-12-14 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0005_auto_20221213_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipos',
            name='fechaExpiracion',
            field=models.DateField(verbose_name='Fecha de expiracion'),
        ),
        migrations.AlterField(
            model_name='trabajadores',
            name='equipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pagina.equipos'),
        ),
    ]
