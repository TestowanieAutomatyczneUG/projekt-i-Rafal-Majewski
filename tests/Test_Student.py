import unittest
from modules.Student import Student


class Test_Student_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Student, [])

	def test_missing_lastName(self):
		with self.assertRaises(TypeError):
			Student(firstName="Jan")

	def test_missing_firstName(self):
		with self.assertRaises(TypeError):
			Student(lastName="Kowalski")
