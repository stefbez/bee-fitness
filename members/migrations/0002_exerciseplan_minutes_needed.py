# Generated by Django 3.1.6 on 2021-03-05 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseplan',
            name='minutes_needed',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
