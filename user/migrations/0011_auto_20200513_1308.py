# Generated by Django 3.0.5 on 2020-05-13 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_geodata_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geodata',
            name='phone1',
            field=models.CharField(max_length=13, null=True, verbose_name='Leave empty if you donot want to show it'),
        ),
    ]
