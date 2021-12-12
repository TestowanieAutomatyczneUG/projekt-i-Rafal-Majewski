import unittest
from modules.Person import Person


class Test_Person_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Person, [])
