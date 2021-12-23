import unittest
from modules.TeacherView import TeacherView
from modules.Teacher import Teacher
from modules.Student import Student
from modules.Grade import Grade
from modules.Subject import Subject
from modules.GradeValue import GradeValue
from modules.Comment import Comment
from datetime import datetime as Datetime


class Test_TeacherView_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, TeacherView)

	def test_correct(self):
		teacher = Teacher(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517"
		)
		TeacherView(teacher=teacher)


class Test_TeacherView_giveGrade(unittest.TestCase):
	def test_return_value(self):
		subject = Subject(id="test", name="Math")
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
		self.assertIs(teacherView.giveGrade(student, grade), grade)

	def test_wrong_subject(self):
		subject = Subject(id="test", name="Math")
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
		subject = Subject(id="test", name="Math")
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

	def test_if_adds(self):
		subject = Subject(id="test", name="Math")
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
		teacherView.giveGrade(student, grade)
		self.assertIn(grade, student.grades)


class Test_takeGrade(unittest.TestCase):
	def test_return_value(self):
		subject = Subject(id="test", name="Math")
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
		teacherView.giveGrade(student, grade)
		self.assertIs(teacherView.takeGrade(student, grade), grade)

	def test_if_removes(self):
		subject = Subject(id="test", name="Math")
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
		teacherView.giveGrade(student, grade)
		teacherView.takeGrade(student, grade)
		self.assertNotIn(grade, student.grades)

	def test_wrong_subject(self):
		subject = Subject(id="test", name="Math")
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
		teacherView.giveGrade(student, grade)
		student.unassignSubject(subject)
		with self.assertRaises(ValueError):
			teacherView.takeGrade(student, grade)

	def test_wrong_teacher(self):
		subject = Subject(id="test", name="Math")
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
		teacherView.giveGrade(student, grade)
		teacher.unassignSubject(subject)
		with self.assertRaises(ValueError):
			teacherView.takeGrade(student, grade)


class Test_giveComment(unittest.TestCase):
	def test_wrong_type(self):
		subject = Subject(id="test", name="Math")
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
		comment = 2
		with self.assertRaises(TypeError):
			teacherView.giveComment(student, comment)

	def test_wrong_teacher(self):
		teacher1 = Teacher(
			firstName="John",
			lastName="Smith",
			pesel="96071361238",
		)
		teacher2 = Teacher(
			firstName="John2",
			lastName="Smith2",
			pesel="80062141433",
		)
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
		)
		teacherView = TeacherView(teacher1)
		datetime = Datetime(year=2020, month=1, day=1)
		comment = Comment(
			teacher=teacher2,
			content="test",
			datetime=datetime,
		)
		with self.assertRaises(ValueError):
			teacherView.giveComment(student, comment)

	def test_correct_return_value(self):
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
		)
		teacher = Teacher(
			firstName="John",
			lastName="Smith",
			pesel="96071361238",
		)
		teacherView = TeacherView(teacher)
		datetime = Datetime(year=2020, month=1, day=1)
		comment = Comment(
			teacher=teacher,
			datetime=datetime,
			content="test"
		)
		self.assertIs(teacherView.giveComment(student, comment), comment)

	def test_if_adds(self):
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
		)
		teacher = Teacher(
			firstName="John",
			lastName="Smith",
			pesel="96071361238",
		)
		teacherView = TeacherView(teacher)
		datetime = Datetime(year=2020, month=1, day=1)
		comment = Comment(
			teacher=teacher,
			datetime=datetime,
			content="test"
		)
		teacherView.giveComment(student, comment)
		self.assertIn(comment, student.comments)


class Test_takeComment(unittest.TestCase):
	def test_correct_return_value(self):
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
		)
		teacher = Teacher(
			firstName="John",
			lastName="Smith",
			pesel="96071361238",
		)
		teacherView = TeacherView(teacher)
		datetime = Datetime(year=2020, month=1, day=1)
		comment = Comment(
			teacher=teacher,
			datetime=datetime,
			content="test"
		)
		teacherView.giveComment(student, comment)
		self.assertIs(teacherView.takeComment(student, comment), comment)

	def test_if_removes(self):
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
		)
		teacher = Teacher(
			firstName="John",
			lastName="Smith",
			pesel="96071361238",
		)
		teacherView = TeacherView(teacher)
		datetime = Datetime(year=2020, month=1, day=1)
		comment = Comment(
			teacher=teacher,
			datetime=datetime,
			content="test"
		)
		teacherView.giveComment(student, comment)
		teacherView.takeComment(student, comment)
		self.assertNotIn(comment, student.comments)

	def test_wrong_type(self):
		student = Student(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
		)
		teacher = Teacher(
			firstName="John",
			lastName="Smith",
			pesel="96071361238",
		)
		teacherView = TeacherView(teacher)
		datetime = Datetime(year=2020, month=1, day=1)
		comment = Comment(
			teacher=teacher,
			datetime=datetime,
			content="test"
		)
		teacherView.giveComment(student, comment)
		with self.assertRaises(TypeError):
			teacherView.takeComment(student, 2)
