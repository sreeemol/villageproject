# Generated by Django 3.2 on 2021-05-07 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('villageapp', '0003_remove_employees_panchayath'),
    ]

    operations = [
        migrations.CreateModel(
            name='enduser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('jobtitle', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
            ],
        ),
    ]
