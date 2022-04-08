# Generated by Django 4.0.3 on 2022-04-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('price', models.IntegerField()),
                ('bpm', models.IntegerField()),
                ('cover', models.ImageField(upload_to='images/')),
                ('beat', models.FileField(upload_to='beats/')),
                ('link', models.CharField(default='', max_length=70)),
            ],
        ),
    ]
