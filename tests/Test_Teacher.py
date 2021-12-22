import unittest
from modules.Teacher import Teacher
from modules.Subject import Subject


class Test_Teacher_constructor(unittest.TestCase):
	def test_no_arguments(self):
		with self.assertRaises(TypeError):
			Teacher()

	def test_with_subjects(self):
		subjects = set([
			Subject(id="test", name="Math"),
			Subject(id="test2", name="Physics"),
		])
		teacher = Teacher(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=subjects
		)
		self.assertEqual(teacher.subjects, subjects)


class Test_unassignSubject(unittest.TestCase):
	def test_if_removes_from_subjects(self):
		subject = Subject(id="test", name="Matematyka")
		teacher = Teacher(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=[subject]
		)
		teacher.unassignSubject(subject)
		self.assertNotIn(subject, teacher.subjects)

	def test_nonexistent(self):
		subject1 = Subject(id="test", name="Matematyka")
		subject2 = Subject(id="test2", name="Fizyka")
		teacher = Teacher(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=[subject1]
		)
		with self.assertRaises(ValueError):
			teacher.unassignSubject(subject2)


class Test_assignSubject(unittest.TestCase):
	def test_wrong_type(self):
		teacher = Teacher(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
		)
		with self.assertRaises(TypeError):
			teacher.assignSubject("test")
