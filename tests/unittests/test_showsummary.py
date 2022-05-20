import pytest

from server import app, clubs, show_summary

@pytest.fixture
def valid_mail():
	return next(c['email'] for c in clubs)

@pytest.fixture
def invalid_mail():
	mails = [c['email'] for c in clubs]
	return ''.join(m[i] if len(m) < i else '_' for i, m in enumerate(mails))

def test_response(valid_mail):
	app.testing
	with app.test_client() as c:
		r = c.post('/showSummary', data={'email': valid_mail})
		assert r.status_code == 200

def test_invalidmail(invalid_mail):
	app.testing
	with app.test_client() as c:
		r = c.post('/showSummary', data={'email': invalid_mail})
		assert r.status_code == 302