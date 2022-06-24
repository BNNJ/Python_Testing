import pytest
from flask import get_flashed_messages

import server
from utils import get_item

def test_valid_competition(mocker):
	club = get_item(server.clubs, lambda x: x['name'] == "simple_club")
	competition = get_item(server.competitions, lambda x: x['name'] == "simple_competition")
	mocker.patch.object(server, 'club', club)

	server.app.testing
	with server.app.test_client() as c:
		r = c.get(f"/book/{competition['name']}")
		flashed_messages = get_flashed_messages()

	assert r.status_code == 200
	assert "<title>Booking for simple_competition || GUDLFT</title>" in str(r.data)
	assert flashed_messages == []

def test_past_competition(mocker):
	club = get_item(server.clubs, lambda x: x['name'] == "simple_club")
	competition = get_item(server.competitions, lambda x: x['name'] == "past_competition")
	mocker.patch.object(server, 'club', club)

	server.app.testing
	with server.app.test_client() as c:
		r = c.get(f"/book/{competition['name']}")
		flashed_messages = get_flashed_messages()

	assert r.status_code == 302
	assert 'You should be redirected automatically to the target URL: <a href="/showSummary">/showSummary</a>' in str(r.data)
	assert "This competition has already taken place" in flashed_messages
