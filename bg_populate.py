import requests
import pandas as pd
import json
import xml.etree.ElementTree as ET
from bgg_recommender.models import SuggestedNumPlayersModel, SuggestedPlayerAgeModel, BoardGameCategoryModel, BoardGameMechanicModel, BoardGameFamily, BoardGameExpansionModel, BoardGameInegrationModel, BoardGameImplementationModel, BoardGameCompilationModel, BoardGameDesignerModel, BoardGameArtistModel, BoardGamePublisherModel, BoardGameModel
import time

games = pd.read_csv('C:\\Users\\Joanna\\Desktop\\bgg_project\\bgg_products.csv')

def attributes(attrib_type, ids=False):
	link = [elem for elem in root[0].findall('link')]
	value = [v.attrib for v in link]
	if attrib_type in list_attributes_with_id:
		ids=True
	if ids:
		return {int(v['id']):v['value'] for v in value if v['type'] == attrib_type}
	else:
		return [v['value'] for v in value if v['type'] == attrib_type]

list_of_attributes = ['boardgamecategory', 'boardgamemechanic', 'boardgamefamily', 'boardgameexpansion', 'boardgameintegration', 'boardgamecompilation', 'boardgamedesigner', 'boardgameartist', 'boardgamepublisher', 'boardgameimplementation' ]
list_attributes_with_id = ['boardgameexpansion', 'boardgameintegration', 'boardgamecompilation', 'boardgameimplementation']

for game in games['ID'].tolist():
	print(games['ID'].tolist().index(game))
	request = requests.get('https://www.boardgamegeek.com/xmlapi2/thing?id={}'.format(game))
	api_content = request.content
	print(request.status_code)
	root = ET.fromstring(api_content)
	thumbnail_image = root[0].find('thumbnail').text
	description_g = root[0].find('description').text
	yearpublished = int(root[0].find('yearpublished').attrib['value'])
	minplayers = int(root[0].find('minplayers').attrib['value'])
	maxplayers = int(root[0].find('maxplayers').attrib['value'])
	suggested_num_players_poll = root[0].find('.//poll[@name="suggested_numplayers"]')
	suggested_num_players_totalvotes = suggested_num_players_poll.attrib['totalvotes']
	suggested_num_players_dict = pd.DataFrame({int(result.attrib['numplayers']): {"best":int(result.find('.//result[@value="Best"]').attrib['numvotes']), "recommended":int(result.find('.//result[@value="Recommended"]').attrib['numvotes']), "not_recommended":int(result.find('.//result[@value="Not Recommended"]').attrib['numvotes'])} for result in suggested_num_players_poll.findall('results')[:-1]}).T.loc[minplayers:maxplayers]
	numplayers = suggested_num_players_dict.idxmax()
	vote_num_players = suggested_num_players_dict.max()
	suggested_players_age_poll = root[0].find('.//poll[@name="suggested_playerage"]')
	suggested_player_age_totalvotes = int(suggested_players_age_poll.attrib['totalvotes'])
	suggested_player_age = pd.DataFrame([poll.attrib for poll in suggested_players_age_poll.findall('.//result')]).set_index('value').astype({"numvotes":int}).sort_values(by='numvotes', ascending=False).index.tolist()[:3]
	language_dependence_poll = root[0].find('.//poll[@name="language_dependence"]')
	language_dependence = pd.DataFrame([poll.attrib for poll in language_dependence_poll.findall('.//result')]).set_index('value').astype({'numvotes':int}).drop(columns='level').sort_values(by='numvotes', ascending=False).index.tolist()[0]
	category_data = dict(zip(list_of_attributes, list(map(attributes, list_of_attributes))))
	min_playtime = int(root[0].find('minplaytime').attrib['value'])
	max_playtime = int(root[0].find('maxplaytime').attrib['value'])
	min_age = int(root[0].find('minage').attrib['value'])
	title = games.loc[games['ID']==game]['Name'].tolist()[0]
	snpm=SuggestedNumPlayersModel.objects.create(totalvotes=suggested_num_players_totalvotes, best_numvotes=vote_num_players['best'], best_numplayers=numplayers['best'], recommended_numvotes=vote_num_players['recommended'], recommended_numplayers=numplayers['recommended'], notrecommended_numvotes=vote_num_players['not_recommended'], notrecommended_numplayers=numplayers['not_recommended'])
	snpm.save()
	spam=SuggestedPlayerAgeModel.objects.create(totalvotes=suggested_num_players_totalvotes, best_playerage=suggested_player_age[0], secondbest_playerage=suggested_player_age[1], thirdbest_playerage=suggested_player_age[2])
	spam.save()
	g = BoardGameModel.objects.create(id_product=game, name=title, description=description_g, year_Published=yearpublished, min_players=minplayers, max_players=maxplayers, minplaytime=min_playtime, maxplaytime=max_playtime, minage=min_age, language_dependency=language_dependence, thumbnail=thumbnail_image, suggested_num_players=snpm, suggested_age_players=spam)
	if category_data['boardgamecategory']:
		for cat in category_data['boardgamecategory']:
			bg_cat = BoardGameCategoryModel.objects.create(category=cat)
			g.categories.add(bg_cat)
			
	if category_data['boardgamemechanic']:										 
		for mech in category_data['boardgamemechanic']:
			bg_mech = BoardGameMechanicModel.objects.create(mechanic=mech)
			g.mechanics.add(bg_mech)
			
	if category_data['boardgamefamily']:												 
		for family in category_data['boardgamefamily']:
			f = family.split(': ')
			bgf = BoardGameFamily.objects.create(genre = f[0], value = f[1])
			g.families.add(bgf)
	
	if category_data['boardgameexpansion']:
		for expansion in category_data['boardgameexpansion']:
			bg_exp = BoardGameExpansionModel.objects.create(id_expansion=expansion, name=category_data['boardgameexpansion'][expansion])
			g.expansions.add(bg_exp)
	
	if category_data['boardgameintegration']:	
		for integration in category_data['boardgameintegration']:
			bg_int = BoardGameInegrationModel.objects.create(id_integration=integration, name=category_data['boardgameintegration'][integration])
			g.integrations.add(bg_int)
			
	if category_data['boardgameimplementation']:	
		for implementation in category_data['boardgameimplementation']:
			bg_imp = BoardGameImplementationModel.objects.create(id_implementation=implementation, name=category_data['boardgameimplementation'][implementation])
			g.implementations.add(bg_imp)

	if category_data['boardgamecompilation']:			
		for compilation in category_data['boardgamecompilation']:
			bg_comp = BoardGameCompilationModel.objects.create(id_compilation=compilation, name=category_data['boardgamecompilation'][compilation])
			g.compilations.add(bg_comp)

	if category_data['boardgamedesigner']:		
		for des in category_data['boardgamedesigner']:
			bg_des = BoardGameDesignerModel.objects.create(name=des)
			g.designers.add(bg_des)

	if category_data['boardgameartist']:	
		for art in category_data['boardgameartist']:
			bg_art = BoardGameArtistModel.objects.create(name=art)
			g.artists.add(bg_art)

	if category_data['boardgamepublisher']:
		for pub in category_data['boardgamepublisher']:
			bg_pub = BoardGamePublisherModel.objects.create(name=pub)
			g.publishers.add(bg_pub)
	g.save()
	time.sleep(1)