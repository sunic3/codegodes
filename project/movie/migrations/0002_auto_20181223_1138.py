# Generated by Django 2.1.4 on 2018-12-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='date of birthday'),
        ),
    ]
