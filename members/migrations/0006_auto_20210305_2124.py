# Generated by Django 3.1.6 on 2021-03-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20210305_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseplan',
            name='cooldown_time',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='main_exercise_time',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='warmup_time',
            field=models.IntegerField(blank=True),
        ),
    ]
