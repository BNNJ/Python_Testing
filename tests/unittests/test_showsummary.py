import pytest

from server import app

def test_response(valid_mail):
	app.testing
	with app.test_client() as c:
		r = c.post('/showSummary', data={'email': valid_mail})
	assert valid_mail == "simple@mail.com"
	assert r.status_code == 200
	assert valid_mail in str(r.data)

def test_invalidmail(inexistent_mail):
	app.testing
	with app.test_client() as c:
		r = c.post('/showSummary', data={'email': inexistent_mail})
	assert r.status_code == 302
