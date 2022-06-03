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
			'name': "low_points",
			'email': "lowpoints@mail.com",
			'points': 2
		},
		{
			'name': "lots_of_points",
			'email': "lotsofpoints@mail.com",
			'points': 123
		},
	]
	mocker.patch.object(server, 'clubs', clubs)

@pytest.fixture
def simple_club():
	return server.clubs[0]

@pytest.fixture
def no_points_club():
	return server.clubs[1]

@pytest.fixture
def lots_of_points_club():
	return server.clubs[3]

@pytest.fixture
def valid_mail():
	return server.clubs[0]['email']

@pytest.fixture
def invalid_mail():
	return "invalid_mail@"

@pytest.fixture
def inexistent_mail():
	return "fakemail@mail.com"


@pytest.fixture(autouse=True)
def test_competitions(mocker):
	competitions = [
		{
			'name': "simple_competition",
			'date': "2023-06-27 10:00:00",
			'numberOfPlaces': 13
		},
		{
			'name': "few_places",
			'date': "2023-06-27 10:00:00",
			'numberOfPlaces': 3
		},
		{
			'name': "no_places_left",
			'date': "2020-03-27 10:00:00",
			'numberOfPlaces': 0
		},
		{
			'name': "1_21_gigawatts",
			'date': "2112-12-21 21:12:21",
			'numberOfPlaces': 121
		},
		{
			'name': "past_competition",
			'date': "1986-05-29 10:00:00",
			'numberOfPlaces': 42
		},
	]
	mocker.patch.object(server, 'competitions', competitions)


@pytest.fixture
def simple_competition():
	return server.competitions[0]

@pytest.fixture
def no_places_competition():
	return server.competitions[2]

@pytest.fixture
def far_future_competition():
	return server.competitions[3]

@pytest.fixture
def past_competition():
	return server.competitions[4]

