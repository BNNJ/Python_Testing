import pytest
from flask import get_flashed_messages

import server
from utils import get_item

def test_valid_purchase(mocker):
	club = get_item(server.clubs, lambda x: x['name'] == "simple_club")
	competition = get_item(server.competitions, lambda x: x['name'] == "simple_competition")
	mocker.patch.object(server, 'club', club)
	current_points = club['points']

	server.app.testing
	with server.app.test_client() as c:
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': 2
		}
		r = c.post('/purchasePlaces', data=data)

	assert competition['name'] == "simple_competition"
	assert club['name'] == "simple_club"
	assert r.status_code == 302
	assert club['points'] == current_points - 2

def test_not_enough_points(mocker):
	club = get_item(server.clubs, lambda x: x['name'] == "low_points")
	competition = get_item(server.competitions, lambda x: x['name'] == "simple_competition")
	mocker.patch.object(server, 'club', club)
	current_points = club['points']

	server.app.testing
	with server.app.test_client() as c:
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': 10
		}
		r = c.post('/purchasePlaces', data=data)
		flashed_messages = get_flashed_messages()

	assert r.status_code == 302
	assert "You don't have enough points to book that many places" in flashed_messages
	assert club['points'] == current_points

def test_more_than_12_places(mocker):
	club = get_item(server.clubs, lambda x: x['name'] == "simple_club")
	competition = get_item(server.competitions, lambda x: x['name'] == "simple_competition")
	mocker.patch.object(server, 'club', club)
	current_points = club['points']

	server.app.testing
	with server.app.test_client() as c:
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': 15
		}
		r = c.post('/purchasePlaces', data=data)
		flashed_messages = get_flashed_messages()

	assert r.status_code == 302
	assert "You can't request more than 12 places" in flashed_messages
	assert club['points'] == current_points

def test_less_than_1_place(mocker):
	club = get_item(server.clubs, lambda x: x['name'] == "simple_club")
	competition = get_item(server.competitions, lambda x: x['name'] == "simple_competition")
	mocker.patch.object(server, 'club', club)
	current_points = club['points']

	server.app.testing
	with server.app.test_client() as c:
		data = {
			'club': club['name'],
			'competition': competition['name'],
			'places': -2
		}
		r = c.post('/purchasePlaces', data=data)
		flashed_messages = get_flashed_messages()

	assert r.status_code == 302
	assert "Invalid number of places requested" in flashed_messages
	assert club['points'] == current_points
	