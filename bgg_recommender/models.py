from django.db import models

# Create your models here.
class BoardGameModel(models.Model):
    id_product = models.IntegerField()
    name = models.CharField(max_length=200)
    description = models.CharField(blank=True, null=True, max_length=10000)
    year_Published = models.IntegerField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    minplaytime = IntegerField()
    maxplaytime = IntegerField()
    minage = IntegerField()
    language_dependency = moddels.CharField(max_length=100)

class SuggestedNumPlayersModel(models.Model):
    id_product = 
    totalvotes = models.IntegerField()
    best_numvotes = models.IntegerField()
    best_numplayers = models.IntegerField
    recommended_numvotes = models.IntegerField()
    recommended_numplayers = models.IntegerField()
    notrecommended_numvotes = models.IntegerField()
    notrecommended_numplayers = models.IntegerField()

class SuggestedPlayerAgeModel(models.Model):
    id_product = 
    totalvotes =  models.IntegerField()
    best_playerage = IntegerField()
    secondbest_playerage = IntegerField()
    thirdbest_playerage = IntegerField()

class BoardGameCategoryModel(models.Model):
    id_product = 
    category = models.CharField(max_length=200)

class BoardGameMechanicModel(models.Model):
    id_product = 
    mechanic = models.CharField(max_length=200)

class BoardGameFamily(models.Model):
    genre = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class BoardGameExpansionModel(models.Model):
    id_product = 
    id_expansion = models.IntegerField()
    name = models.CharField(max_length=200)

class BoardGameInegrationModel(models.Model):
    id_product = 
    id_integration = models.IntegerField()
    name = models.CharField(max_length=200)

class BoardGameImplementationModel(models.Model):
    id_product = 
    id_implementation = models.IntegerField()
    name = models.CharField(max_length=200)

class BoardGameCompilationModel(models.Model):
    id_product = 
    id_compilation = models.IntegerField()
    name = models.CharField(max_length=200)

class BoardGameDesignerModel(models.Model):
    id_product =
    name = models.CharField(max_length=100)

class BoardGameArtistModel(models.Model):
    id_product =
    name = models.CharField(max_length=100)

class BoardGamePublisherModel(models.Model):
    id_product =
    name = models.CharField(max_length=100)

