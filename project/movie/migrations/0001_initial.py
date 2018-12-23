# Generated by Django 2.1.4 on 2018-12-23 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('login', models.CharField(max_length=255, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('date', models.DateField()),
                ('data', models.TextField(blank=True, default='', null=True, verbose_name='Activated movies')),
                ('snils', models.CharField(blank=True, default='snils', max_length=255, null=True, unique=True, verbose_name='SNILS')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('date', models.CharField(default='', max_length=100, verbose_name='date of release')),
                ('age', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('cost', models.IntegerField(default=0)),
                ('time', models.IntegerField(default=7200)),
                ('director', models.CharField(max_length=100)),
                ('roles', models.TextField(default='')),
                ('pos', models.IntegerField()),
                ('neg', models.IntegerField()),
                ('image', models.FileField(upload_to='')),
                ('trailer', models.CharField(max_length=100)),
                ('link', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('categories', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('small_title', models.TextField()),
                ('large_title', models.TextField()),
            ],
        ),
    ]
