# Generated by Django 4.0.3 on 2022-04-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ankeansite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='time',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
