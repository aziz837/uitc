# Generated by Django 3.1.4 on 2021-04-23 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bootcamp', '0020_auto_20210423_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('photo', models.ImageField(null=True, upload_to='profile')),
                ('price', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='payment_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='courser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bootcamp.courser'),
        ),
    ]
