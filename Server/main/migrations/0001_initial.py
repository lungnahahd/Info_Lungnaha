# Generated by Django 3.1.4 on 2021-01-27 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='infolist',
            fields=[
                ('title', models.CharField(max_length=30)),
                ('information', models.CharField(max_length=500)),
                ('now', models.DateTimeField()),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]