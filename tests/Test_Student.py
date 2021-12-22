import unittest
from modules.Student import Student
from modules.Subject import Subject


class Test_Student_constructor(unittest.TestCase):
	def test_no_arguments(self):
		with self.assertRaises(TypeError):
			Student()

	def test_only_firstName(self):
		with self.assertRaises(TypeError):
			Student(firstName="Jan")

	def test_only_lastName(self):
		with self.assertRaises(TypeError):
			Student(lastName="Kowalski")

	def test_with_subjects(self):
		subjects = set([
			Subject(id="test", name="Math"),
			Subject(id="test2", name="Physics"),
		])
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=subjects
		)
		self.assertEqual(student.subjects, subjects)


class Test_edit_Student(unittest.TestCase):
	def test_change_firstName(self):
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		student.firstName = "Adam"
		self.assertEqual(student.firstName, "Adam")

	def test_change_lastName(self):
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		student.lastName = "Nowak"
		self.assertEqual(student.lastName, "Nowak")


class Test_assignSubject(unittest.TestCase):
	def test_correct_in_constructor(self):
		subject = Subject(id="test", name="Matematyka")
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=set([subject])
		)
		self.assertIn(subject, student.subjects)

	def test_return_value(self):
		subject = Subject(id="test", name="Matematyka")
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		self.assertIs(student.assignSubject(subject), subject)

	def test_correct_manually(self):
		subject = Subject(id="test", name="Matematyka")
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		student.assignSubject(subject)
		self.assertIn(subject, student.subjects)

	def test_incorrect_manually(self):
		subject = 2
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		self.assertRaises(TypeError, student.assignSubject, subject)


class Test_unassignSubject(unittest.TestCase):
	def test_if_removes_from_subjects(self):
		subject = Subject(id="test", name="Matematyka")
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
		subject = Subject(id="test", name="Matematyka")
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=set([subject])
		)
		self.assertIs(student.unassignSubject(subject), subject)
