# Generated by Django 3.1.6 on 2021-03-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0007_auto_20210307_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]
