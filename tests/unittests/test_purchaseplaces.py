import pytest

from server import app

def test_response(simple_club, simple_competition):
	app.testing
	data = {
		'club': simple_club['name'],
		'competition': simple_competition['name']
	}
	with app.test_client() as c:
		r = c.post('/purchasePlaces', data=data)
	assert r.status_code == 200
	
	# assert simple_competition['name'] == "simple_competition"