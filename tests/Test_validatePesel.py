import unittest
from parameterized import parameterized  # type: ignore
from hamcrest import assert_that, is_
from modules.utils import validatePesel


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
		pesels = []
		with open("./tests/data/valid_pesels.txt") as file:
			for line in file:
				trimmedLine = line.strip()
				if trimmedLine:
					pesels.append(trimmedLine)
		for pesel in pesels:
			assert_that(validatePesel(pesel), is_(True))
