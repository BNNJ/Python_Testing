import pytest
from flask import get_flashed_messages

import server
from utils import get_item

def test_showsummary(mocker):
	club = get_item(server.clubs, lambda x: x['name'] == "simple_club")
	competition = get_item(
		server.competitions,
		lambda x: x['name'] == "simple_competition"
	)
	mocker.patch.object(server, 'club', club)

	server.app.testing
	with server.app.test_client() as c:
		r = c.get('/showSummary')

	assert r.status_code == 200
	assert f"<h2>Welcome, {club['email']} </h2>" in str(r.data)
	