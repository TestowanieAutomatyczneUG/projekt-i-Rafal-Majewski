import unittest
from modules.Subject import Subject


class Test_Subject_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Subject)

	def test_name(self):
		subject = Subject(id="test", name="Math")
		self.assertEqual(subject.name, "Math")

	def test_incorrect_name(self):
		with self.assertRaises(TypeError):
			Subject(id="test", name=123)

	def test_id(self):
		subject = Subject(id="test", name="Math")
		self.assertEqual(subject.id, "test")
