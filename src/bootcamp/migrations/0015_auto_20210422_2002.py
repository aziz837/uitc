# Generated by Django 3.1.4 on 2021-04-22 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp', '0014_auto_20210422_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=15, null=True)),
                ('year', models.CharField(max_length=15, null=True)),
                ('photo', models.ImageField(null=True, upload_to='profile')),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
