import pytest

from server import app

def test_response(valid_mail):
	app.testing
	with app.test_client() as c:
		r = c.post('/showSummary', data={'email': valid_mail})
	assert r.status_code == 200

def test_invalidmail(inexistent_mail):
	app.testing
	with app.test_client() as c:
		r = c.post('/showSummary', data={'email': inexistent_mail})
	assert r.status_code == 302