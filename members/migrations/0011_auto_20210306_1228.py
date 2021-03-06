# Generated by Django 3.1.6 on 2021-03-06 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_auto_20210305_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exerciseplan',
            name='cooldown_instructions',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='cooldown_time',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='warmup_instructions',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='exerciseplan',
            name='warmup_time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]