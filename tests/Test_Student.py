import unittest
from modules.Student import Student
from modules.Subject import Subject
from modules.Grade import Grade
from modules.GradeValue import GradeValue
from modules.Teacher import Teacher
from datetime import datetime as Datetime


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

	def test_nonexistent(self):
		subject1 = Subject(id="test", name="Matematyka")
		subject2 = Subject(id="test2", name="Fizyka")
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=set([subject1])
		)
		with self.assertRaises(ValueError):
			student.unassignSubject(subject2)


class Test_Student_removeReferencesToTeacher(unittest.TestCase):
	def test_with_teacher_if_removes(self):
		subject = Subject(id="test", name="Matematyka")
		teacher1 = Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		teacher2 = Teacher(firstName="Adam", lastName="Nowak", pesel="02231887245")
		grade1 = Grade(
			value=GradeValue.G1PLUS,
			datetime=Datetime(2018, 1, 1),
			teacher=teacher1,
			subject=subject,
		)
		grade2 = Grade(
			value=GradeValue.G1PLUS,
			datetime=Datetime(2018, 1, 1),
			teacher=teacher2,
			subject=subject,
		)
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			grades=[grade1, grade2],
			subjects=[subject],
		)
		student.removeReferencesToTeacher(teacher1)
		self.assertNotIn(grade1, student.grades)

	def test_with_teacher_wrong_type(self):
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517"
		)
		with self.assertRaises(TypeError):
			student.removeReferencesToTeacher("Jan")


class Test_removeReferencesToSubject(unittest.TestCase):
	def test_grades(self):
		subject = Subject(id="test", name="Matematyka")
		grade = Grade(
			value=GradeValue.G1PLUS,
			datetime=Datetime(2018, 1, 1),
			subject=subject,
			teacher=Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		)
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=[subject],
			grades=[grade],
		)
		student.removeReferencesToSubject(subject)
		self.assertNotIn(grade, student.grades)


class Test_addGrade(unittest.TestCase):
	def test_wrong_type(self):
		student = Student(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		with self.assertRaises(TypeError):
			student.addGrade("grade")
