# Generated by Django 3.2.4 on 2022-09-27 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webzine', '0006_auto_20220925_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='blind_webzine',
            name='is_blind',
            field=models.CharField(default='true', editable=False, max_length=5),
        ),
    ]
