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
	assert 'target URL: <a href="/showSummary">/showSummary</a>' in str(r.data)

def test_login_invalidmail():
	email = "thisemaildoesntexist@fakemail.com"

	server.app.testing
	with server.app.test_client() as c:
		r = c.post('/login', data={'email': email})
		flashed_messages = get_flashed_messages()

	assert r.status_code == 302
	assert "No club with this email was found" in flashed_messages
	assert 'target URL: <a href="/">/</a>' in str(r.data)

def test_logout():
	server.app.testing
	with server.app.test_client() as c:
		r = c.get('/logout')
		flashed_messages = get_flashed_messages()

	assert r.status_code == 302
	assert 'target URL: <a href="/">/</a>' in str(r.data)
	assert "Goodbye, see you soon!" in flashed_messages
