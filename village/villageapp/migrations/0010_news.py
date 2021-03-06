# Generated by Django 3.2 on 2021-05-11 02:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('villageapp', '0009_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=100)),
                ('panchayath', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='News', to='villageapp.panchayath')),
            ],
        ),
    ]
