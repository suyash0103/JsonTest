# Generated by Django 3.0.7 on 2020-07-08 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jsontestapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activityperiod',
            name='tz',
        ),
        migrations.AddField(
            model_name='users',
            name='tz',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
