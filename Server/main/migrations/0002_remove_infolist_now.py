# Generated by Django 3.1.4 on 2021-02-17 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infolist',
            name='now',
        ),
    ]