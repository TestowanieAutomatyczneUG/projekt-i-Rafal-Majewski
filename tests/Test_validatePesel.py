import unittest
from parameterized import parameterized  # type: ignore
from hamcrest import assert_that, is_
from modules.utils import validatePesel


def load(filepath: str) -> list[str]:
	trimmedLines = []
	with open(filepath) as file:
		for line in file:
			trimmedLine = line.strip()
			if trimmedLine:
				trimmedLines.append(trimmedLine)
	return trimmedLines


class Test_validatePesel(unittest.TestCase):
	def test_correct(self):
		assert_that(validatePesel("97092537961"), is_(True))

	def test_non_digit(self):
		assert_that(validatePesel("9709a537961"), is_(False))

	def test_incorrect_month(self):
		assert_that(validatePesel("97142537969"), is_(False))

	def test_incorrect_day(self):
		assert_that(validatePesel("97093537961"), is_(False))

	@parameterized.expand([
		"77070138891",
		"05290866323",
		"63070469217",
		"86071681772",
		"00262842997",
	])
	def test_incorrect_checksum(self, pesel: str):
		assert_that(validatePesel(pesel), is_(False))

	def test_too_short(self):
		assert_that(validatePesel("123456789"), is_(False))

	def test_too_long(self):
		assert_that(validatePesel("1234567890123"), is_(False))

	def test_many_valid_pesels(self):
		pesels = load("./tests/data/valid_pesels.txt")
		for pesel in pesels:
			assert_that(validatePesel(pesel), is_(True))

	def test_many_invalid_pesels(self):
		pesels = load("./tests/data/invalid_pesels.txt")
		for pesel in pesels:
			assert_that(validatePesel(pesel), is_(False))
