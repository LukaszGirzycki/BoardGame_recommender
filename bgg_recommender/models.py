from django.db import models

# Create your models here.
class SuggestedNumPlayersModel(models.Model):
    totalvotes = models.IntegerField()
    best_numvotes = models.IntegerField()
    best_numplayers = models.IntegerField(null=True)
    recommended_numvotes = models.IntegerField()
    recommended_numplayers = models.IntegerField()
    notrecommended_numvotes = models.IntegerField()
    notrecommended_numplayers = models.IntegerField()

class SuggestedPlayerAgeModel(models.Model):
    totalvotes =  models.IntegerField()
    best_playerage = models.IntegerField()
    secondbest_playerage = models.IntegerField()
    thirdbest_playerage = models.IntegerField()

class BoardGameCategoryModel(models.Model):
    category = models.CharField(max_length=200)

class BoardGameMechanicModel(models.Model):
    mechanic = models.CharField(max_length=200)

class BoardGameFamily(models.Model):
    genre = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class BoardGameExpansionModel(models.Model):
    id_expansion = models.IntegerField()
    name = models.CharField(max_length=200)

class BoardGameInegrationModel(models.Model):
    id_integration = models.IntegerField()
    name = models.CharField(max_length=200)

class BoardGameImplementationModel(models.Model):
    id_implementation = models.IntegerField()
    name = models.CharField(max_length=200)

class BoardGameCompilationModel(models.Model):
    id_compilation = models.IntegerField()
    name = models.CharField(max_length=200)

class BoardGameDesignerModel(models.Model):
    name = models.CharField(max_length=100)

class BoardGameArtistModel(models.Model):
    name = models.CharField(max_length=100)

class BoardGamePublisherModel(models.Model):
    name = models.CharField(max_length=100)

class BoardGameModel(models.Model):
    id_product = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(blank=True, null=True, max_length=10000)
    year_Published = models.IntegerField(blank=True, null=True)
    min_players = models.IntegerField(blank=True, null=True)
    max_players = models.IntegerField(blank=True, null=True)
    minplaytime = models.IntegerField(blank=True, null=True)
    maxplaytime = models.IntegerField(blank=True, null=True)
    minage = models.IntegerField(blank=True, null=True)
    language_dependency = models.CharField(blank=True, null=True, max_length=100)
    suggested_num_players = models.OneToOneField(SuggestedNumPlayersModel, on_delete=models.CASCADE, primary_key=False, blank=True, null=True)
    suggested_age_players = models.OneToOneField(SuggestedPlayerAgeModel, on_delete=models.CASCADE, primary_key=False, blank=True, null=True)
    categories = models.ManyToManyField(BoardGameCategoryModel, blank=True)
    mechanics = models.ManyToManyField(BoardGameMechanicModel, blank=True)
    families = models.ManyToManyField(BoardGameFamily, blank=True)
    expansions = models.ManyToManyField(BoardGameExpansionModel, blank=True)
    integrations = models.ManyToManyField(BoardGameInegrationModel, blank=True)
    implementations = models.ManyToManyField(BoardGameImplementationModel, blank=True)
    compilations = models.ManyToManyField(BoardGameCompilationModel, blank=True)
    designers = models.ManyToManyField(BoardGameDesignerModel, blank=True)
    artists = models.ManyToManyField(BoardGameArtistModel, blank=True)
    publishers = models.ManyToManyField(BoardGamePublisherModel, blank=True)
    thumbnail = models.URLField(blank=True, null=True)