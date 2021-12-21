import unittest
from modules.Teacher import Teacher


class Test_Teacher_constructor(unittest.TestCase):
	def test_no_arguments(self):
		with self.assertRaises(TypeError):
			Teacher()
