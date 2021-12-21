import unittest
from modules.Teacher import Teacher
from modules.Subject import Subject


class Test_Teacher_constructor(unittest.TestCase):
	def test_no_arguments(self):
		with self.assertRaises(TypeError):
			Teacher()

	def test_with_subjects(self):
		subjects = set([
			Subject(name="Math"),
			Subject(name="Physics"),
		])
		teacher = Teacher(
			firstName="Jan",
			lastName="Kowalski",
			pesel="85052342517",
			subjects=subjects
		)
		self.assertEqual(teacher.subjects, subjects)
