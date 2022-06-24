import pytest

import server

def test_displayboard():
	server.app.testing
	with server.app.test_client() as c:
		r = c.get('/displayBoard')

	assert r.status_code == 200
	for club in server.clubs:
		assert f"<td>{club['name']}</td>" in str(r.data)