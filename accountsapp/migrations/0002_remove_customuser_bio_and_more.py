# Generated by Django 5.1.4 on 2024-12-12 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountsapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_picture',
        ),
    ]
