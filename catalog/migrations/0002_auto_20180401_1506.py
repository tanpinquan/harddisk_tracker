# Generated by Django 2.0.3 on 2018-04-01 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hdd',
            options={'ordering': ['name']},
        ),
    ]
