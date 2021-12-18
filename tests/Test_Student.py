import unittest
from modules.Student import Student
from modules.Subject import Subject


class Test_Student_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Student, [])

	def test_only_firstName(self):
		with self.assertRaises(TypeError):
			Student(firstName="Jan")

	def test_only_lastName(self):
		with self.assertRaises(TypeError):
			Student(lastName="Kowalski")


class Test_edit_Student(unittest.TestCase):
	def test_change_firstName(self):
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		student.firstName = "Adam"
		self.assertEqual(student.firstName, "Adam")

	def test_change_lastName(self):
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		student.lastName = "Nowak"
		self.assertEqual(student.lastName, "Nowak")


class Test_assign_subject_toStudent(unittest.TestCase):
	def test_correct_in_constructor(self):
		subject = Subject(name="Matematyka")
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=set([subject])
		)
		self.assertIn(subject, student.subjects)

	def test_correct_manually(self):
		subject = Subject(name="Matematyka")
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		student.assignSubject(subject)
		self.assertIn(subject, student.subjects)

	def test_incorrect_manually(self):
		subject = 2
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		self.assertRaises(TypeError, student.assignSubject, subject)
