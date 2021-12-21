import unittest
from modules.Subject import Subject


class Test_Subject_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Subject)

	def test_name(self):
		subject = Subject(name="Math")
		self.assertEqual(subject.name, "Math")