# Generated by Django 2.1.5 on 2019-02-16 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
