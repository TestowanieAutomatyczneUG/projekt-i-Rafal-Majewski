import unittest
from modules.TeacherView import TeacherView
from modules.Gradebook import Gradebook
from modules.Teacher import Teacher


class Test_TeacherView_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, TeacherView)

	def test_correct(self):
		gradebook = Gradebook(schoolName="Test")
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		TeacherView(gradebook=gradebook, teacher=teacher)
