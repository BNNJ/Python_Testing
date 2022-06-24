import pytest
from flask import get_flashed_messages

import server
from utils import get_item

def test_login():
	club = get_item(server.clubs, lambda x: x['name'] == "simple_club")
	email = club['email']

	server.app.testing
	with server.app.test_client() as c:
		r = c.post('/login', data={'email': email})
		flashed_messages = get_flashed_messages()

	assert r.status_code == 302
	assert flashed_messages == []
	assert server.club is club
	assert 'You should be redirected automatically to target URL: <a href="/showSummary">/showSummary</a>' in str(r.data)

def test_invalidmail():
	email = "thisemaildoesntexist@fakemail.com"

	server.app.testing
	with server.app.test_client() as c:
		r = c.post('/login', data={'email': email})
		flashed_messages = get_flashed_messages()

	assert r.status_code == 302
	assert "No club with this email was found" in flashed_messages
	assert 'You should be redirected automatically to target URL: <a href="/">/</a>' in str(r.data)

def test_showsummary(mocker):
	club = get_item(server.clubs, lambda x: x['name'] == "simple_club")
	competition = get_item(server.competitions, lambda x: x['name'] == "simple_competition")
	mocker.patch.object(server, 'club', club)

	server.app.testing
	with server.app.test_client() as c:
		r = c.get('/showSummary')

	assert r.status_code == 200
	assert "<title>Summary | GUDLFT Registration</title>" in str(r.data)
	assert f"<h2>Welcome, {club['email']} </h2>" in str(r.data)
