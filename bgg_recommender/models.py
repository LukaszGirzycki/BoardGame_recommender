from django.db import models

# Create your models here.
class SuggestedNumPlayersModel(models.Model):
    vote_num_players_dict = models.CharField(max_length=1000, null=True, blank=True)

class SuggestedPlayerAgeModel(models.Model):
    totalvotes =  models.IntegerField()
    best_playerage = models.IntegerField()
    secondbest_playerage = models.IntegerField()
    thirdbest_playerage = models.IntegerField()
    def __str__(self):
        return str(self.best_playerage)

class BoardGameCategoryModel(models.Model):
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.category

class BoardGameMechanicModel(models.Model):
    mechanic = models.CharField(max_length=200)
    def __str__(self):
        return self.mechanic

class BoardGameFamilyModel(models.Model):
    genre = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    def __str__(self):
        return "{genre}: {value}".format(genre=self.genre, value=self.value)

class BoardGameExpansionModel(models.Model):
    id_expansion = models.IntegerField()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class BoardGameIntegrationModel(models.Model):
    id_integration = models.IntegerField()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class BoardGameImplementationModel(models.Model):
    id_implementation = models.IntegerField()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class BoardGameCompilationModel(models.Model):
    id_compilation = models.IntegerField()
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class BoardGameDesignerModel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class BoardGameArtistModel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class BoardGamePublisherModel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class StatBoardGameModel(models.Model):
    usersrated = models.IntegerField()
    average = models.FloatField()
    stddev = models.FloatField()
    owned = models.IntegerField()
    trading = models.IntegerField()
    wanting = models.IntegerField()
    wishing = models.IntegerField()
    num_comments = models.IntegerField()
    num_weights = models.IntegerField()
    average_weight = models.FloatField()

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
    suggested_num_players = models.ForeignKey(SuggestedNumPlayersModel, on_delete=models.CASCADE, primary_key=False, blank=True, null=True)
    suggested_age_players = models.OneToOneField(SuggestedPlayerAgeModel, on_delete=models.CASCADE, primary_key=False, blank=True, null=True)
    categories = models.ManyToManyField(BoardGameCategoryModel, blank=True)
    mechanics = models.ManyToManyField(BoardGameMechanicModel, blank=True)
    families = models.ManyToManyField(BoardGameFamilyModel, blank=True)
    expansions = models.ManyToManyField(BoardGameExpansionModel, blank=True)
    integrations = models.ManyToManyField(BoardGameIntegrationModel, blank=True)
    implementations = models.ManyToManyField(BoardGameImplementationModel, blank=True)
    compilations = models.ManyToManyField(BoardGameCompilationModel, blank=True)
    designers = models.ManyToManyField(BoardGameDesignerModel, blank=True)
    artists = models.ManyToManyField(BoardGameArtistModel, blank=True)
    publishers = models.ManyToManyField(BoardGamePublisherModel, blank=True)
    thumbnail = models.URLField(blank=True, null=True)
    stats = models.OneToOneField(StatBoardGameModel, on_delete=models.CASCADE, primary_key=False, blank=True, null=True)

class RankingBoardGameModel(models.Model):
    friendly_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    bayesaverage = models.FloatField()
    boardgame = models.ForeignKey(BoardGameModel, on_delete=models.CASCADE, null=True, blank=True)