import pytest

from server import app

def test_response(simple_club, simple_competition):
	app.testing
	with app.test_client() as c:
		r = c.get(f"/book/{simple_competition['name']}/{simple_club['name']}")
	assert r.status_code == 200

def test_old_competition(simple_club, past_competition):
	app.testing
	with app.test_client() as c:
		r = c.get(f"/book/{past_competition['name']}/{simple_club['name']}")
	assert r.status_code == 200
	assert "This competition has already taken place" in str(r.data)

def test_future_competition(simple_club, future_competition):
	app.testing
	with app.test_client() as c:
		r = c.get(f"/book/{future_competition['name']}/{simple_club['name']}")
	assert r.status_code == 200
	assert "This competition has already taken place" not in str(r.data)