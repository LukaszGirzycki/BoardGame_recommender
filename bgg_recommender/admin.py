from django.contrib import admin
from bgg_recommender.models import BoardGameModel

# Register your models here.
class BoardGameAdmin(admin.ModelAdmin):
    list_display= ('name', 'year_Published', 'min_players', 'max_players', 'minplaytime', 'maxplaytime', 'suggested_num_players', 'suggested_age_players')
    list_filter = ('min_players', 'max_players', 'minplaytime', 'maxplaytime', 'categories', 'mechanics', 'families')
    search_fields = ('id_product', 'name',)

admin.site.register(BoardGameModel, BoardGameAdmin)
