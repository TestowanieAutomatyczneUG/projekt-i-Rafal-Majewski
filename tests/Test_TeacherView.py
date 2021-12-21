import unittest
from modules.TeacherView import TeacherView
from modules.Gradebook import Gradebook
from modules.Teacher import Teacher
from modules.Student import Student
from modules.Grade import Grade
from modules.Subject import Subject
from modules.GradeValue import GradeValue
from datetime import datetime as Datetime


class Test_TeacherView_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, TeacherView)

	def test_correct(self):
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		TeacherView(teacher=teacher)


class Test_TeacherView_giveGrade(unittest.TestCase):
	def test_return_value(self):
		subject = Subject(name="Math")
		gradebook = Gradebook(schoolName="Test", subjects=[subject])
		student = gradebook.addStudent(
			Student(
				firstName="Jan",
				lastName="Kowalski",
				pesel="85052342517",
				subjects=[subject]
			)
		)
		teacher = gradebook.addTeacher(
			Teacher(
				firstName="John",
				lastName="Smith",
				pesel="96071361238",
				subjects=[subject]
			)
		)
		teacherView = TeacherView(teacher)
		datetime = Datetime(year=2020, month=1, day=1)
		grade = Grade(
			teacher=teacher,
			subject=subject,
			datetime=datetime,
			value=GradeValue.G3PLUS
		)
		self.assertIs(teacherView.giveGrade(student, grade), grade)

	def test_wrong_subject(self):
		subject = Subject(name="Math")
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=[]
		)
		teacher = Teacher(
			firstName="John",
			lastName="Smith",
			pesel="96071361238",
			subjects=[subject]
		)
		teacherView = TeacherView(teacher)
		datetime = Datetime(year=2020, month=1, day=1)
		grade = Grade(
			teacher=teacher,
			subject=subject,
			datetime=datetime,
			value=GradeValue.G3PLUS
		)
		with self.assertRaises(ValueError):
			teacherView.giveGrade(student, grade)

	def test_wrong_teacher(self):
		subject = Subject(name="Math")
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=[subject]
		)
		teacher = Teacher(
			firstName="John",
			lastName="Smith",
			pesel="96071361238",
			subjects=[]
		)
		teacherView = TeacherView(teacher)
		datetime = Datetime(year=2020, month=1, day=1)
		grade = Grade(
			teacher=teacher,
			subject=subject,
			datetime=datetime,
			value=GradeValue.G3PLUS
		)
		with self.assertRaises(ValueError):
			teacherView.giveGrade(student, grade)


class Test_takeGrade(unittest.TestCase):
	def test_return_value(self):
		subject = Subject(name="Math")
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=[subject]
		)
		teacher = Teacher(
			firstName="John",
			lastName="Smith",
			pesel="96071361238",
			subjects=[subject]
		)
		teacherView = TeacherView(teacher)
		datetime = Datetime(year=2020, month=1, day=1)
		grade = Grade(
			teacher=teacher,
			subject=subject,
			datetime=datetime,
			value=GradeValue.G3PLUS
		)
		student.addGrade(grade)
		self.assertIs(teacherView.takeGrade(student, grade), grade)
