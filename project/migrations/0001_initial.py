# Generated by Django 4.0.4 on 2022-04-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('cdate', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('place', models.CharField(max_length=30)),
                ('link', models.CharField(max_length=30)),
                ('tag', models.CharField(max_length=10)),
                ('proceeding', models.CharField(default='진행중', max_length=10)),
                ('poster', models.ImageField(upload_to='')),
                ('content', models.TextField()),
                ('isVisible', models.CharField(default='true', max_length=10)),
            ],
        ),
    ]
