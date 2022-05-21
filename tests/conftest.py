import pytest

import server

@pytest.fixture(autouse=True)
def test_clubs(mocker):
	clubs = [
		{
			'name': "simple_club",
			'email': "simple@mail.com",
			'points': 8
		},
		{
			'name': "no_points",
			'email': "nopoints@mail.com",
			'points': 0
		},
		{
			'name': "lots_of_points",
			'email': "lotsofpoints@mail.com",
			'points': 123
		},
	]
	mocker.patch.object(server, 'clubs', clubs)

@pytest.fixture
def valid_mail():
	return "simple@mail.com"

@pytest.fixture
def invalid_mail():
	return "invalid_mail@"

@pytest.fixture
def inexistent_mail():
	return "fakemail@mail.com"