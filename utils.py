import json
from datetime import datetime


def load_clubs(filename):
    with open(filename, "r") as f:
        list_of_clubs = json.load(f)["clubs"]
    for club in list_of_clubs:
        club["points"] = int(club["points"])
    return list_of_clubs


def load_competitions(filename):
    with open(filename, "r") as f:
        list_of_competitions = json.load(f)["competitions"]
    for competition in list_of_competitions:
        competition["numberOfPlaces"] = int(competition["numberOfPlaces"])
    return list_of_competitions


def get_item(iterable, predicat):
    return next((item for item in iterable if predicat(item)), None)


def date_is_past(datestr, formatstr="%Y-%m-%d %H:%M:%S"):
    return datetime.strptime(datestr, formatstr) < datetime.now()


def purchase_error(requested, available):
    if requested > 12:
        return "You can't request more than 12 places"
    elif requested <= 0:
        return "Invalid number of places requested"
    elif requested > available:
        return "You don't have enough points to book that many places"
    else:
        return None
