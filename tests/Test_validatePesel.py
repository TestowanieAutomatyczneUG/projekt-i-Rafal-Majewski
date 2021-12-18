import unittest
from modules.utils import validatePesel
from parameterized import parameterized  # type: ignore


class Test_validatePesel(unittest.TestCase):
	def test_wrong_length(self):
		self.assertFalse(validatePesel("123456789"))

	def test_correct(self):
		self.assertTrue(validatePesel("97092537961"))

	def test_non_digit(self):
		self.assertFalse(validatePesel("9709a537961"))

	def test_incorrect_month(self):
		self.assertFalse(validatePesel("97142537969"))

	def test_incorrect_day(self):
		self.assertFalse(validatePesel("97093537961"))

	@parameterized.expand([
		"77070138891",
		"05290866323",
		"63070469217",
		"86071681772",
		"00262842997",
	])
	def test_incorrect_checksum(self, pesel: str):
		self.assertFalse(validatePesel(pesel))
