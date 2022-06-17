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

class TestLoadClub:

	@staticmethod
	def test_load():
		clubs = load_clubs("tests/test_clubs.json")
		expected = 4
		actual = len(clubs)

		assert expected == actual
