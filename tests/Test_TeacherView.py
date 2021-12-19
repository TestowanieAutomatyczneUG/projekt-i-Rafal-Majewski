import unittest
from modules.TeacherView import TeacherView


class Test_TeacherView_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, TeacherView)
