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

@pytest.fixture(autouse=True)
def test_competitions(mocker):
	competitions = [
		{
			'name': "simple_competition",
			'date': "2033-06-27 10:00:00",
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
