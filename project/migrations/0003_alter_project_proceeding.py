# Generated by Django 4.0.4 on 2022-06-22 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_alter_project_proceeding_remove_project_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proceeding',
            field=models.CharField(choices=[('진행중', '진행중'), ('진행예정', '진행예정'), ('마감', '마감')], default='진행중', max_length=10),
        ),
    ]