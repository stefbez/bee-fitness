# Generated by Django 3.1.6 on 2021-03-05 23:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20210305_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='exerciseplan',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=80),
            preserve_default=False,
        ),
    ]
