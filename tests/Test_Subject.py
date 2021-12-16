import unittest
from modules.Subject import Subject


class Test_Subject_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Subject)
