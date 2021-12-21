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
		subject = Subject(name="Math")
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		datetime = Datetime(year=2020, month=1, day=1)
		Grade(
			subject=subject,
			teacher=teacher,
			value=GradeValue.G3PLUS,
			datetime=datetime
		)
