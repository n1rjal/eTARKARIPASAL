# Generated by Django 3.0.5 on 2020-05-10 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200510_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='geodata',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
