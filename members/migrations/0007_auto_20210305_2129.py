# Generated by Django 3.1.6 on 2021-03-05 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20210305_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseplan',
            name='cooldown_time',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='main_exercise_time',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='warmup_time',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]