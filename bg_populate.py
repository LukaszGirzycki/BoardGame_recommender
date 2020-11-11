import requests
import pandas as pd
import json
import xml.etree.ElementTree as ET
from bgg_recommender.models import SuggestedNumPlayersModel, SuggestedPlayerAgeModel, BoardGameCategoryModel, BoardGameMechanicModel, BoardGameFamilyModel, BoardGameExpansionModel, BoardGameIntegrationModel, BoardGameImplementationModel, BoardGameCompilationModel, BoardGameDesignerModel, BoardGameArtistModel, BoardGamePublisherModel, StatBoardGameModel, RankingBoardGameModel, BoardGameModel
import time
games = pd.read_csv('C:\\Users\\Joanna\\Desktop\\bgg_project\\errors.csv').reset_index().rename(columns={'index':'ID'})
#games = pd.read_csv('C:\\Users\\Joanna\\Desktop\\bgg_project\\bgg_products.csv')

error_dict = {}
n=1
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
	print('games id: '+str(game))
	print('index: '+str(games['ID'].tolist().index(game)))
	request = requests.get('https://www.boardgamegeek.com/xmlapi2/thing?id={}&stats=1'.format(game))
	print(request.status_code)
	stop = 60
	while request.status_code == 202 or request.status_code == 429:
		print(stop)
		time.sleep(stop)
		request = requests.get('https://www.boardgamegeek.com/xmlapi2/thing?id={}'.format(game))
		stop+=60
		n+=1
		
	api_content = request.content
	root = ET.fromstring(api_content)
	#try:
	if root[0].find('thumbnail') != None:
		thumbnail_image = root[0].find('thumbnail').text
	else:
		thumbnail_image = 0
	if root[0].find('description') != None:
		description_g = root[0].find('description').text
	else:
		description_g = 0
	yearpublished = int(root[0].find('yearpublished').attrib['value'])
	minplayers = int(root[0].find('minplayers').attrib['value'])
	maxplayers = int(root[0].find('maxplayers').attrib['value'])
	suggested_num_players_poll = root[0].find('.//poll[@name="suggested_numplayers"]')
	suggested_num_players_totalvotes = int(suggested_num_players_poll.attrib['totalvotes'])
	if suggested_num_players_totalvotes != 0:
		if suggested_num_players_poll.findall('results')[0].attrib['numplayers'] == '0+':
			suggested_num_players_dict = {0: 'other'}
		elif minplayers > maxplayers:
			suggested_num_players_dict = pd.DataFrame({int(result.attrib['numplayers']): {"best":int(result.find('.//result[@value="Best"]').attrib['numvotes']), "recommended":int(result.find('.//result[@value="Recommended"]').attrib['numvotes']), "not_recommended":int(result.find('.//result[@value="Not Recommended"]').attrib['numvotes'])} for result in suggested_num_players_poll.findall('results')}).T.loc[maxplayers:minplayers].T.to_dict()
		else:
			suggested_num_players_dict = pd.DataFrame({int(result.attrib['numplayers']): {"best":int(result.find('.//result[@value="Best"]').attrib['numvotes']), "recommended":int(result.find('.//result[@value="Recommended"]').attrib['numvotes']), "not_recommended":int(result.find('.//result[@value="Not Recommended"]').attrib['numvotes'])} for result in suggested_num_players_poll.findall('results')[:-1]}).T.loc[minplayers:maxplayers].T.to_dict()
		
	else:
		suggested_num_players_dict = None
	snpm=SuggestedNumPlayersModel.objects.create(vote_num_players_dict=str(suggested_num_players_dict))
	snpm.save()
		
	suggested_players_age_poll = root[0].find('.//poll[@name="suggested_playerage"]')
	suggested_player_age_totalvotes = int(suggested_players_age_poll.attrib['totalvotes'])
	if suggested_player_age_totalvotes != 0:
		suggested_player_age = pd.DataFrame([poll.attrib for poll in suggested_players_age_poll.findall('.//result')]).set_index('value').astype({"numvotes":int}).sort_values(by='numvotes', ascending=False).filter(axis=0, regex='^\d+$').index.tolist()[:3]
	else:
		suggested_player_age = [0, 0, 0]
	language_dependence_poll = root[0].find('.//poll[@name="language_dependence"]')
	if int(language_dependence_poll.attrib['totalvotes']) != 0:
		language_dependence = pd.DataFrame([poll.attrib for poll in language_dependence_poll.findall('.//result')]).set_index('value').astype({'numvotes':int}).drop(columns='level').sort_values(by='numvotes', ascending=False).index.tolist()[0]
	else:
		language_dependence = "There is no votes"
	category_data = dict(zip(list_of_attributes, list(map(attributes, list_of_attributes))))
	min_playtime = int(root[0].find('minplaytime').attrib['value'])
	max_playtime = int(root[0].find('maxplaytime').attrib['value'])
	min_age = int(root[0].find('minage').attrib['value'])
	title = [el for el in root[0].findall('name') if el.attrib['type']=='primary'][0].attrib['value']
	stats = root[0].find('statistics')[0]
	usersrated = int(stats.find('usersrated').attrib['value'])
	ranks = [rank.attrib for rank in stats.find('ranks')]
	stddev = float(stats.find('stddev').attrib['value'])
	owned = int(stats.find('owned').attrib['value'])
	trading = int(stats.find('trading').attrib['value'])
	wanting = int(stats.find('wanting').attrib['value'])
	wishing = int(stats.find('wishing').attrib['value'])
	average = float(stats.find('average').attrib['value'])
	num_comments = int(stats.find('numcomments').attrib['value'])
	num_weights = int(stats.find('numweights').attrib['value'])
	average_weight = float(stats.find('averageweight').attrib['value'])
	
	sbgm = StatBoardGameModel.objects.create(usersrated=usersrated, average = average, stddev=stddev, owned=owned, trading=trading, wanting=wanting, wishing=wishing, num_comments=num_comments, num_weights=num_weights, average_weight=average_weight)
	
	spam=SuggestedPlayerAgeModel.objects.create(totalvotes=suggested_num_players_totalvotes, best_playerage=suggested_player_age[0], secondbest_playerage=suggested_player_age[1], thirdbest_playerage=suggested_player_age[2])
	spam.save()
	
	g = BoardGameModel.objects.create(id_product=game, name=title, description=description_g, year_Published=yearpublished, min_players=minplayers, max_players=maxplayers, minplaytime=min_playtime, maxplaytime=max_playtime, minage=min_age, language_dependency=language_dependence, thumbnail=thumbnail_image, suggested_num_players=snpm, suggested_age_players=spam, stats=sbgm)

	for rank_type in ranks:
		print(rank_type)
		print(g)
		if rank_type['value'] == 'Not Ranked':
			rank_type['value'] = 0
			rank_type['bayesaverage'] = 0
		rbgm = RankingBoardGameModel.objects.create(name=rank_type['name'], friendly_name=rank_type['friendlyname'], value=rank_type['value'], bayesaverage=rank_type['bayesaverage'], boardgame=g)
		rbgm.save()
		
	if category_data['boardgamecategory']:
		for cat in category_data['boardgamecategory']:
			bg_cat = BoardGameCategoryModel.objects.get_or_create(category=cat)
			g.categories.add(bg_cat[0])

	if category_data['boardgamemechanic']:						 
		for mech in category_data['boardgamemechanic']:
			bg_mech = BoardGameMechanicModel.objects.get_or_create(mechanic=mech)
			g.mechanics.add(bg_mech[0])

	if category_data['boardgamefamily']:
		for family in category_data['boardgamefamily']:
			f = family.split(': ')
			if len(f) == 1:
				bgf = BoardGameFamilyModel.objects.get_or_create(genre = "other", value = f[0])
			else:
				bgf = BoardGameFamilyModel.objects.get_or_create(genre = f[0], value = f[1])
			g.families.add(bgf[0])

	if category_data['boardgameexpansion']:
		for expansion in category_data['boardgameexpansion']:
			bg_exp = BoardGameExpansionModel.objects.get_or_create(id_expansion=expansion, name=category_data['boardgameexpansion'][expansion])
			g.expansions.add(bg_exp[0])

	if category_data['boardgameintegration']:
		for integration in category_data['boardgameintegration']:
			bg_int = BoardGameIntegrationModel.objects.get_or_create(id_integration=integration, name=category_data['boardgameintegration'][integration])
			g.integrations.add(bg_int[0])

	if category_data['boardgameimplementation']:	
		for implementation in category_data['boardgameimplementation']:
			bg_imp = BoardGameImplementationModel.objects.get_or_create(id_implementation=implementation, name=category_data['boardgameimplementation'][implementation])
			g.implementations.add(bg_imp[0])

	if category_data['boardgamecompilation']:			
		for compilation in category_data['boardgamecompilation']:
			bg_comp = BoardGameCompilationModel.objects.get_or_create(id_compilation=compilation, name=category_data['boardgamecompilation'][compilation])
			g.compilations.add(bg_comp[0])

	if category_data['boardgamedesigner']:		
		for des in category_data['boardgamedesigner']:
			bg_des = BoardGameDesignerModel.objects.get_or_create(name=des)
			g.designers.add(bg_des[0])

	if category_data['boardgameartist']:	
		for art in category_data['boardgameartist']:
			bg_art = BoardGameArtistModel.objects.get_or_create(name=art)
			g.artists.add(bg_art[0])

	if category_data['boardgamepublisher']:
		for pub in category_data['boardgamepublisher']:
			bg_pub = BoardGamePublisherModel.objects.get_or_create(name=pub)
			g.publishers.add(bg_pub[0])
	g.save()
	#except Exception as exception:
	#	print(exception)
	#	error_dict[game] = str(exception)
	time.sleep(n)

pd.DataFrame([error_dict]).T.to_csv('C:\\Users\\Joanna\\Desktop\\bgg_project\\errors2.csv')