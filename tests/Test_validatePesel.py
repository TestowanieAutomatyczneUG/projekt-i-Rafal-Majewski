import unittest
from modules.utils import validatePesel


class Test_validatePesel(unittest.TestCase):
	def test_wrong_length(self):
		self.assertFalse(validatePesel("123456789"))

	def test_correct(self):
		self.assertTrue(validatePesel("97092537961"))

	def test_non_digit(self):
		self.assertFalse(validatePesel("9709a537961"))

	def test_incorrect_month(self):
		self.assertFalse(validatePesel("97142537969"))
