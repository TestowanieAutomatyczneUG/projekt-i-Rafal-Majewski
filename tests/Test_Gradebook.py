import unittest
from modules.Gradebook import Gradebook


class Test_Gradebook(unittest.TestCase):
	def test_constructor_no_arguments(self):
		self.assertRaises(TypeError, Gradebook, [])

	def test_constructor_correct_name(self):
		gradebook = Gradebook(schoolName="Test")
		self.assertEqual(gradebook.schoolName, "Test")
