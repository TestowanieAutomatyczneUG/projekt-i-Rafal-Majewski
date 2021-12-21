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


class Test_assign_subject_to_Student(unittest.TestCase):
	def test_correct_in_constructor(self):
		subject = Subject(name="Matematyka")
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=set([subject])
		)
		self.assertIn(subject, student.subjects)

	def test_return_value(self):
		subject = Subject(name="Matematyka")
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		self.assertIs(student.assignSubject(subject), subject)

	def test_correct_manually(self):
		subject = Subject(name="Matematyka")
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		student.assignSubject(subject)
		self.assertIn(subject, student.subjects)

	def test_incorrect_manually(self):
		subject = 2
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		self.assertRaises(TypeError, student.assignSubject, subject)


class Test_unassign_subject_from_Student(unittest.TestCase):
	def test_if_removes_from_subjects(self):
		subject = Subject(name="Matematyka")
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=set([subject])
		)
		student.unassignSubject(subject)

	def test_wrong_type(self):
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517"
		)
		with self.assertRaises(TypeError):
			student.unassignSubject("informatyka")

	def test_return_value(self):
		subject = Subject(name="Matematyka")
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=set([subject])
		)
		self.assertIs(student.unassignSubject(subject), subject)
