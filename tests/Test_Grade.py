import unittest
from modules.Grade import Grade


class Test_Grade_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Grade)
