# Generated by Django 2.1.7 on 2019-03-09 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Database', '0002_auto_20190309_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
