import unittest
from modules.Gradebook import Gradebook
from modules.Student import Student
from modules.Teacher import Teacher
from modules.Subject import Subject


class Test_Gradebook_constructor(unittest.TestCase):
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


class Test_Gradebook_addStudent(unittest.TestCase):
	def test_return_value_when_correct(self):
		gradebook = Gradebook(schoolName="Test")
		student = gradebook.addStudent(Student(
			firstName="Test", lastName="Test", pesel="85052342517"
		))
		self.assertIsInstance(student, Student)

	def test_if_adds_when_correct(self):
		gradebook = Gradebook(schoolName="Test")
		student = gradebook.addStudent(Student(
			firstName="Test", lastName="Test", pesel="85052342517"
		))
		self.assertIn(student, gradebook.students)


class Test_Gradebook_addTeacher(unittest.TestCase):
	def test_correct(self):
		gradebook = Gradebook(schoolName="Test")
		teacher = gradebook.addTeacher(Teacher(
			firstName="Test", lastName="Test", pesel="85052342517"
		))
		self.assertIsInstance(teacher, Teacher)


class Test_Gradebook_removeStudent(unittest.TestCase):
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
		subject = Subject(name="Test subject")
		with self.assertRaises(AttributeError):
			gradebook.subjects.add(subject)
