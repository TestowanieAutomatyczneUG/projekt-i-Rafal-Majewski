import unittest
from modules.Gradebook import Gradebook
from modules.Student import Student
from modules.Teacher import Teacher
from modules.Subject import Subject
from modules.Grade import Grade
from datetime import datetime as Datetime
from modules.GradeValue import GradeValue


class Test_Gradebook_constructor(unittest.TestCase):
	def test_with_teachers(self):
		teachers = set([
			Teacher(pesel="85052342517", firstName="Jan", lastName="Kowalski"),
			Teacher(pesel="52010961958", firstName="Adam", lastName="Nowak"),
		])
		gradebook = Gradebook(teachers=teachers, schoolName="Test")
		self.assertEqual(gradebook.teachers, teachers)

	def test_with_students(self):
		students = set([
			Student(pesel="85052342517", firstName="Jan", lastName="Kowalski"),
			Student(pesel="52010961958", firstName="Adam", lastName="Nowak"),
		])
		gradebook = Gradebook(schoolName="Test", students=students)
		self.assertEqual(gradebook.students, students)

	def test_no_arguments(self):
		self.assertRaises(TypeError, Gradebook)

	def test_correct_name(self):
		gradebook = Gradebook(schoolName="Test")
		self.assertEqual(gradebook.schoolName, "Test")

	def test_incorrect_name(self):
		with self.assertRaises(ValueError):
			Gradebook(schoolName="")

	def test_name_of_wrong_type(self):
		with self.assertRaises(TypeError):
			Gradebook(schoolName=53)

	def test_with_subjects(self):
		subjects = set([
			Subject(id="a", name="Math"),
			Subject(id="b", name="Physics"),
			Subject(id="c", name="Chemistry"),
		])
		gradebook = Gradebook(schoolName="Test", subjects=subjects)
		self.assertEqual(gradebook.subjects, subjects)

	def test_with_subjects_of_wrong_type(self):
		with self.assertRaises(TypeError):
			Gradebook(schoolName="Test", subjects=53)

	def test_with_teachers_of_wrong_type(self):
		with self.assertRaises(TypeError):
			Gradebook(schoolName="Test", teachers=53)

	def test_with_teacher_of_wrong_type(self):
		teachers = set([
			"teacher1",
		])
		with self.assertRaises(TypeError):
			Gradebook(schoolName="Test", teachers=teachers)


class Test_Gradebook_addStudent(unittest.TestCase):
	def test_return_value_when_correct(self):
		gradebook = Gradebook(schoolName="Test")
		student = Student(firstName="Test", lastName="Test", pesel="85052342517")
		self.assertIs(gradebook.addStudent(student), student)

	def test_if_adds_when_correct(self):
		gradebook = Gradebook(schoolName="Test")
		student = gradebook.addStudent(Student(
			firstName="Test", lastName="Test", pesel="85052342517"
		))
		self.assertIn(student, gradebook.students)

	def test_if_raises_when_pesel_already_exists(self):
		gradebook = Gradebook(schoolName="Test")
		student1 = Student(firstName="Test1", lastName="Test1", pesel="85052342517")
		student2 = Student(firstName="Test2", lastName="Test2", pesel="85052342517")
		gradebook.addStudent(student1)
		with self.assertRaises(ValueError):
			gradebook.addStudent(student2)

	def test_with_student_of_wrong_type(self):
		gradebook = Gradebook(schoolName="Test")
		with self.assertRaises(TypeError):
			gradebook.addStudent(53)


class Test_Gradebook_addSubject(unittest.TestCase):
	def test_if_raises_when_id_already_exists(self):
		gradebook = Gradebook(schoolName="Test")
		subject1 = Subject(id="a", name="Math")
		subject2 = Subject(id="a", name="Math2")
		gradebook.addSubject(subject1)
		with self.assertRaises(ValueError):
			gradebook.addSubject(subject2)

	def test_with_subject_of_wrong_type(self):
		with self.assertRaises(TypeError):
			Gradebook(schoolName="Test").addSubject(53)


class Test_Gradebook_addTeacher(unittest.TestCase):
	def test_correct(self):
		gradebook = Gradebook(schoolName="Test")
		teacher = gradebook.addTeacher(Teacher(
			firstName="Test", lastName="Test", pesel="85052342517"
		))
		self.assertIsInstance(teacher, Teacher)

	def test_if_raises_when_pesel_already_exists(self):
		gradebook = Gradebook(schoolName="Test")
		teacher1 = Teacher(firstName="Test1", lastName="Test1", pesel="85052342517")
		teacher2 = Teacher(firstName="Test2", lastName="Test2", pesel="85052342517")
		gradebook.addTeacher(teacher1)
		with self.assertRaises(ValueError):
			gradebook.addTeacher(teacher2)


class Test_Gradebook_removeStudent(unittest.TestCase):
	def test_nonexistent_student(self):
		student1 = Student(firstName="Test", lastName="Test", pesel="85052342517")
		student2 = Student(firstName="Test2", lastName="Test2", pesel="64022029588")
		gradebook = Gradebook(schoolName="Test", students=[student1])
		with self.assertRaises(ValueError):
			gradebook.removeStudent(student2)

	def test_return_value_when_correct(self):
		gradebook = Gradebook(schoolName="Test")
		student = gradebook.addStudent(Student(
			firstName="Test", lastName="Test", pesel="85052342517"
		))
		self.assertEqual(gradebook.removeStudent(student), student)

	def test_if_removes_when_correct(self):
		gradebook = Gradebook(schoolName="Test")
		student = gradebook.addStudent(Student(
			firstName="Test", lastName="Test", pesel="85052342517"
		))
		gradebook.removeStudent(student)
		self.assertNotIn(student, gradebook.students)


class Test_Gradebook_removeSubject(unittest.TestCase):
	def test_nonexistent_subject(self):
		subject1 = Subject(id="a", name="Math")
		subject2 = Subject(id="b", name="Physics")
		gradebook = Gradebook(schoolName="Test", subjects=[subject1])
		with self.assertRaises(ValueError):
			gradebook.removeSubject(subject2)

	def test_return_value_when_correct(self):
		gradebook = Gradebook(schoolName="Test")
		subject = gradebook.addSubject(Subject(
			id="a", name="Math"
		))
		self.assertEqual(gradebook.removeSubject(subject), subject)

	def test_if_removes_when_correct(self):
		gradebook = Gradebook(schoolName="Test")
		subject = gradebook.addSubject(Subject(
			id="a", name="Math"
		))
		gradebook.removeSubject(subject)
		self.assertNotIn(subject, gradebook.subjects)

	def test_if_removes_from_teachers(self):
		subject = Subject(id="a", name="Math")
		teacher = Teacher(
			firstName="Test",
			lastName="Test",
			pesel="85052342517",
			subjects=[subject]
		)
		gradebook = Gradebook(
			schoolName="Test",
			teachers=[teacher],
			subjects=[subject]
		)
		gradebook.removeSubject(subject)
		self.assertNotIn(subject, teacher.subjects)

	def test_if_removes_from_students(self):
		subject = Subject(id="a", name="Math")
		student = Student(
			firstName="Test",
			lastName="Test",
			pesel="85052342517",
			subjects=[subject]
		)
		gradebook = Gradebook(
			schoolName="Test",
			students=[student],
			subjects=[subject]
		)
		gradebook.removeSubject(subject)
		self.assertNotIn(subject, student.subjects)


class Test_Gradebook_removeTeacher(unittest.TestCase):
	def test_nonexistent_teacher(self):
		teacher1 = Teacher(firstName="Test", lastName="Test", pesel="85052342517")
		teacher2 = Teacher(firstName="Test2", lastName="Test2", pesel="64022029588")
		gradebook = Gradebook(schoolName="Test", teachers=[teacher1])
		with self.assertRaises(ValueError):
			gradebook.removeTeacher(teacher2)

	def test_return_value_when_correct(self):
		gradebook = Gradebook(schoolName="Test")
		teacher = gradebook.addTeacher(Teacher(
			firstName="Test", lastName="Test", pesel="85052342517"
		))
		self.assertEqual(gradebook.removeTeacher(teacher), teacher)

	def test_if_removes_when_correct(self):
		gradebook = Gradebook(schoolName="Test")
		teacher = gradebook.addTeacher(Teacher(
			firstName="Test", lastName="Test", pesel="85052342517"
		))
		gradebook.removeTeacher(teacher)
		self.assertNotIn(teacher, gradebook.teachers)

	def test_with_students(self):
		subject = Subject(id="a", name="Math")
		teacher = Teacher(
			firstName="Test",
			lastName="Test",
			pesel="85052342517",
			subjects=[subject]
		)
		grade = Grade(
			subject=subject,
			teacher=teacher,
			datetime=Datetime(year=2020, month=1, day=1),
			value=GradeValue.G1PLUS
		)
		student = Student(
			firstName="Test",
			lastName="Test",
			pesel="85052342517",
			subjects=[subject],
			grades=[grade]
		)
		gradebook = Gradebook(
			schoolName="Test",
			teachers=[teacher],
			students=[student],
			subjects=[subject]
		)
		gradebook.removeTeacher(teacher)
		self.assertNotIn(grade, student.grades)


class Test_Gradebook_students(unittest.TestCase):
	def test_if_returns_frozenset(self):
		gradebook = Gradebook(schoolName="Test")
		self.assertIsInstance(gradebook.students, frozenset)

	def test_if_empty_at_start(self):
		gradebook = Gradebook(schoolName="Test")
		self.assertFalse(gradebook.students)

	def test_if_not_possible_to_add_student_directly(self):
		gradebook = Gradebook(schoolName="Test")
		student = Student(firstName="Test", lastName="Test", pesel="85052342517")
		with self.assertRaises(AttributeError):
			gradebook.students.add(student)


class Test_Gradebook_subjects(unittest.TestCase):
	def test_if_returns_frozenset(self):
		gradebook = Gradebook(schoolName="Test")
		self.assertIsInstance(gradebook.subjects, frozenset)

	def test_if_empty_at_start(self):
		gradebook = Gradebook(schoolName="Test")
		self.assertFalse(gradebook.subjects)

	def test_if_not_possible_to_add_subject_directly(self):
		gradebook = Gradebook(schoolName="Test school")
		subject = Subject(id="test", name="Test subject")
		with self.assertRaises(AttributeError):
			gradebook.subjects.add(subject)
