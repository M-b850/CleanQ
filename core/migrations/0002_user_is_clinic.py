# Generated by Django 3.2 on 2021-04-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_clinic',
            field=models.BooleanField(default=False),
        ),
    ]