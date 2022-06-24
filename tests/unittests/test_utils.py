import pytest

from utils import (
	load_clubs,
	load_competitions,
	get_item,
	date_is_past,
	purchase_error
)

@pytest.fixture
def haystack():
	return [
		{'foo': "FOO1", 'bar': "BAR1"},
		{'foo': "FOO2", 'bar': "BAR2"},
		{'foo': "FOO3", 'bar': "BAR3"},
		{'foo': "FOO4", 'bar': "BAR4"},
	]

class TestGetItem:

	@staticmethod
	def test_found(haystack):
		expected = {'foo': "FOO3", 'bar': "BAR3"}
		actual = get_item(haystack, lambda c: c['foo'] == "FOO3")
		assert actual == expected

	@staticmethod
	def test_not_found(haystack):
		expected = None
		actual = get_item(haystack, lambda c: c['bar'] == "unkown")
		assert actual is None

	@staticmethod
	def test_invalid_key(haystack):
		expected = None
		with pytest.raises(KeyError):
			actual = get_item(haystack, lambda c: c['baz'] == "invalid")

class TestLoadClubs:

	@staticmethod
	def test_load():
		clubs = load_clubs("tests/test_clubs.json")
		expected = 4
		actual = len(clubs)
		assert expected == actual

	@staticmethod
	def test_file_not_found():
		with pytest.raises(FileNotFoundError):
			clubs = load_clubs("invalid_file.json")

	@staticmethod
	def test_type():
		clubs = load_clubs("tests/test_clubs.json")
		# expected = 'list'
		# actual = type(clubs)
		assert isinstance(clubs, list)

class TestLoadCompetitions:

	@staticmethod
	def test_load():
		competitions = load_competitions("tests/test_competitions.json")
		expected = 5
		actual = len(competitions)
		assert expected == actual

	@staticmethod
	def test_file_not_found():
		with pytest.raises(FileNotFoundError):
			clubs = load_competitions("invalid_file.json")

	@staticmethod
	def test_type():
		competitions = load_competitions("tests/test_competitions.json")
		assert isinstance(competitions, list)

class TestDateIsPast:

	@staticmethod
	def test_past_date():
		date = "1986-05-29 00:00:00"
		expected = True
		actual = date_is_past(date)

		assert expected == actual

	@staticmethod
	def test_future_date():
		date = "2112-12-21 12:21:12"
		expected = False
		actual = date_is_past(date)

		assert expected == actual

	@staticmethod
	def test_invalid_format():
		date = "2112/21/21 12:21:12"
		with pytest.raises(ValueError):
			actual = date_is_past(date)

	@staticmethod
	def	test_invalid_format_string():
		date = "2112/21/21 12:21:12"
		formatstr = "invalid"
		with pytest.raises(ValueError):
			actual = date_is_past(date, formatstr)

class TestPurchaseError:

	@staticmethod
	def test_valid_purchase():
		requested = 5
		available = 9

		expected = None
		actual = purchase_error(requested, available)

		assert actual is expected
	
	@staticmethod
	def test_not_enough_points():
		requested = 4
		available = 2

		expected = "You don't have enough points to book that many places"
		actual = purchase_error(requested, available)

		assert actual == expected

	@staticmethod
	def test_more_than_twelve():
		requested = 21
		available = 42

		expected = "You can't request more than 12 places"
		actual = purchase_error(requested, available)

		assert actual == expected

	@staticmethod
	def test_less_than_one():
		requested = -2
		available = 21

		expected = "Invalid number of places requested"
		actual = purchase_error(requested, available)

		assert actual == expected

	@staticmethod
	def test_more_than_twelve_and_not_enough_points():
		requested = 21
		available = 2

		expected = "You can't request more than 12 places"
		actual = purchase_error(requested, available)

		assert actual == expected
