# Generated by Django 2.1.7 on 2019-03-09 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='first_name',
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
