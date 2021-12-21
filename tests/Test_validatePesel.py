import unittest
from parameterized import parameterized  # type: ignore
from hamcrest import assert_that, not_
from ValidPesel import valid_pesel


class Test_validatePesel(unittest.TestCase):
	def test_wrong_length(self):
		assert_that("12345678901", not_(valid_pesel()))

	def test_correct(self):
		assert_that("97092537961", valid_pesel())

	def test_non_digit(self):
		assert_that("9709a537961", not_(valid_pesel()))

	def test_incorrect_month(self):
		assert_that("97142537969", not_(valid_pesel()))

	def test_incorrect_day(self):
		assert_that("97093537961", not_(valid_pesel()))

	@parameterized.expand([
		"77070138891",
		"05290866323",
		"63070469217",
		"86071681772",
		"00262842997",
	])
	def test_incorrect_checksum(self, pesel: str):
		assert_that(pesel, not_(valid_pesel()))

	def test_too_short(self):
		assert_that("123456789", not_(valid_pesel()))
