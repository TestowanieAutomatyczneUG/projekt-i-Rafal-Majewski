import unittest
from modules.Grade import Grade
from modules.Subject import Subject
from modules.Teacher import Teacher
from modules.GradeValue import GradeValue
from datetime import datetime as Datetime


class Test_Grade_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Grade)

	def test_correct(self):
		subject = Subject(id="test", name="Math")
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		datetime = Datetime(year=2020, month=1, day=1)
		Grade(
			subject=subject,
			teacher=teacher,
			value=GradeValue.G3PLUS,
			datetime=datetime
		)

	def test_teacher_property(self):
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		grade = Grade(
			subject=Subject(id="test", name="Math"),
			teacher=teacher,
			value=GradeValue.G3PLUS,
			datetime=Datetime(year=2020, month=1, day=1)
		)
		self.assertEqual(grade.teacher, teacher)

	def test_incorrect_subject_type(self):
		with self.assertRaises(TypeError):
			Grade(
				subject=1,
				teacher=Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517"),
				value=GradeValue.G3PLUS,
				datetime=Datetime(year=2020, month=1, day=1)
			)

	def test_incorrect_value_type(self):
		with self.assertRaises(TypeError):
			Grade(
				subject=Subject(id="test", name="Math"),
				teacher=Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517"),
				value=1,
				datetime=Datetime(year=2020, month=1, day=1)
			)

	def test_value_property(self):
		grade = Grade(
			subject=Subject(id="test", name="Math"),
			teacher=Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517"),
			value=GradeValue.G3PLUS,
			datetime=Datetime(year=2020, month=1, day=1)
		)
		self.assertEqual(grade.value, GradeValue.G3PLUS)
