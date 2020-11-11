# Generated by Django 3.1.2 on 2020-11-08 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bgg_recommender', '0014_auto_20201108_1605'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardgamemodel',
            name='ranks',
        ),
        migrations.AddField(
            model_name='rankingboardgamemodel',
            name='boardgame',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bgg_recommender.boardgamemodel'),
        ),
    ]
