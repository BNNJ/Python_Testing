import json
from datetime import datetime

def load_clubs():
	with open('clubs.json', 'r') as f:
		list_of_clubs = json.load(f)['clubs']
	return list_of_clubs

def save_clubs(clubs):
	with open('clubs.json', 'w') as f:
		json.dump({'clubs': clubs}, f, indent=2)

def load_competitions():
	with open('competitions.json', 'r') as f:
		list_of_competitions = json.load(f)['competitions']
	return list_of_competitions

def save_competitions(competitions):
	with open('competitions.json', 'w') as f:
		json.dump({'competitions': competitions}, f, indent=2)

def get_item(iterable, predicat):
	return next((item for item in iterable if predicat(item)), None)

def date_is_past(datestr, formatstr="%Y-%m-%d %H:%M:%S"):
	return datetime.strptime(datestr, formatstr) < datetime.now()

def purchase_error(requested, available):
	if requested > 12:
		return "You can't request more than 12 places"
	elif requested > available:
		return "You don't have enough points to book that many places"
	else:
		return None