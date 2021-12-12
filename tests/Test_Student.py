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


class Test_edit_Student(unittest.TestCase):
	def test_change_firstName(self):
		student = Student(firstName="Jan", lastName="Kowalski")
		student.firstName = "Adam"
		self.assertEqual(student.firstName, "Adam")

	def test_change_lastName(self):
		student = Student(firstName="Jan", lastName="Kowalski")
		student.lastName = "Nowak"
		self.assertEqual(student.lastName, "Nowak")
