# Generated by Django 3.1.2 on 2020-10-27 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bgg_recommender', '0003_auto_20201027_1859'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardgameartistmodel',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='boardgamecategorymodel',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='boardgamecompilationmodel',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='boardgamedesignermodel',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='boardgameexpansionmodel',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='boardgamefamily',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='boardgameimplementationmodel',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='boardgameinegrationmodel',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='boardgamemechanicmodel',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='boardgamepublishermodel',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='suggestednumplayersmodel',
            name='id_product',
        ),
        migrations.RemoveField(
            model_name='suggestedplayeragemodel',
            name='id_product',
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='artists',
            field=models.ManyToManyField(to='bgg_recommender.BoardGameArtistModel'),
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='categories',
            field=models.ManyToManyField(to='bgg_recommender.BoardGameCategoryModel'),
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='compilations',
            field=models.ManyToManyField(to='bgg_recommender.BoardGameCompilationModel'),
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='designers',
            field=models.ManyToManyField(to='bgg_recommender.BoardGameDesignerModel'),
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='expansions',
            field=models.ManyToManyField(to='bgg_recommender.BoardGameExpansionModel'),
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='families',
            field=models.ManyToManyField(to='bgg_recommender.BoardGameFamily'),
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='implementations',
            field=models.ManyToManyField(to='bgg_recommender.BoardGameImplementationModel'),
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='integrations',
            field=models.ManyToManyField(to='bgg_recommender.BoardGameInegrationModel'),
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='mechanics',
            field=models.ManyToManyField(to='bgg_recommender.BoardGameMechanicModel'),
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='publishers',
            field=models.ManyToManyField(to='bgg_recommender.BoardGamePublisherModel'),
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='suggested_age_players',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bgg_recommender.suggestedplayeragemodel'),
        ),
        migrations.AddField(
            model_name='boardgamemodel',
            name='suggested_num_players',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bgg_recommender.suggestednumplayersmodel'),
        ),
    ]