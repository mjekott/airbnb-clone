# Generated by Django 2.2.5 on 2021-12-29 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='check_in',
            field=models.TimeField(),
        ),
    ]