# Generated by Django 3.1.2 on 2020-11-08 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bgg_recommender', '0010_auto_20201108_1247'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BoardGameFamily',
            new_name='BoardGameFamilyModel',
        ),
    ]