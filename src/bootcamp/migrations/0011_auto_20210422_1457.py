# Generated by Django 3.1.4 on 2021-04-22 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp', '0010_auto_20210422_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='last_name',
        ),
    ]