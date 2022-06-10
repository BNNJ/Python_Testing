import json

def load_clubs():
	with open('clubs.json', 'r') as f:
		list_of_clubs = json.load(f)['clubs']
	return list_of_clubs

def save_clubs():
	with open('clubs.json', 'w') as f:
		json.dump({'clubs': clubs}, f)

def load_competitions():
	with open('competitions.json', 'r') as f:
		list_of_competitions = json.load(f)['competitions']
	return list_of_competitions

def save_competitions():
	with open('competitions.json', 'w') as f:
		json.dump(f, {'competitions': competitions})

def get_item(iterable, predicat):
	return next((item for item in iterable if predicat(item)), None)