import unittest
from modules.GradeValue import GradeValue
from parameterized import parameterized  # type: ignore


class Test_GradeValue(unittest.TestCase):
	@parameterized.expand([
		("G1", 1),
		("G1PLUS", 1.25),
		("G2MINUS", 1.75),
		("G2", 2),
		("G2PLUS", 2.25),
		("G3MINUS", 2.75),
		("G3", 3),
		("G3PLUS", 3.25),
		("G4MINUS", 3.75),
		("G4", 4),
		("G4PLUS", 4.25),
		("G5MINUS", 4.75),
		("G5", 5),
		("G5PLUS", 5.25),
		("G6MINUS", 5.75),
		("G6", 6)
	])
	def test_GradeValue(self, gradeValueId: str, expectedGradeValueNumber: float):
		self.assertEqual(GradeValue[gradeValueId].value, expectedGradeValueNumber)