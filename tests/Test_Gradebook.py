import unittest
from modules.Gradebook import Gradebook


class Test_Gradebook_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Gradebook, [])

	def test_correct_name(self):
		gradebook = Gradebook(schoolName="Test")
		self.assertEqual(gradebook.schoolName, "Test")

	def test_incorrect_name(self):
		with self.assertRaises(ValueError):
			Gradebook(schoolName="")

	def test_name_of_wrong_type(self):
		with self.assertRaises(TypeError):
			Gradebook(schoolName=53)

