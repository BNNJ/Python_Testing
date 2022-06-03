import pytest

from server import app

def test_response(simple_club, simple_competition):
	app.testing
	with app.test_client() as c:
		data = {
			'club': simple_club['name'],
			'competition': simple_competition['name'],
			'places': 2
		}
		r = c.post('/purchasePlaces', data=data)

	assert simple_competition['name'] == "simple_competition"
	assert simple_club['name'] == "simple_club"
	assert r.status_code == 200

def test_not_enough_points(no_points_club, simple_competition):
	app.testing
	with app.test_client() as c:
		data = {
			'club': no_points_club['name'],
			'competition': simple_competition['name'],
			'places': 24
		}
		r = c.post('/purchasePlaces', data=data)

	assert "You don&#39;t have enough points" in str(r.data)
	# assert r.status_code == 200