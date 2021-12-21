import unittest
from modules.utils import calculatePeselChecksum
from parameterized import parameterized  # type: ignore


class Test_validatePesel(unittest.TestCase):
	@parameterized.expand([
		("8410031846", 3),
		("7911212251", 5),
		("7510158412", 6),
		("4605042773", 8),
		("0425187987", 5),
		("6712039619", 4),
		("4707196611", 4),
		("0129288111", 7),
		("5606035824", 3),
		("7303022179", 4)
	])
	def test_correct(self, peselPart: str, expectedChecksum: int):
		self.assertEqual(calculatePeselChecksum(peselPart), expectedChecksum)

	def test_incorrect_type(self):
		with self.assertRaises(TypeError):
			calculatePeselChecksum(1)

	def test_contains_non_digit(self):
		with self.assertRaises(ValueError):
			calculatePeselChecksum("8410031846a")

	def test_too_long(self):
		with self.assertRaises(ValueError):
			calculatePeselChecksum("8410031846121111")
