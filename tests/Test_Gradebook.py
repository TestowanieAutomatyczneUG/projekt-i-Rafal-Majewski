import unittest
from modules.Gradebook import Gradebook


class Test_Gradebook(unittest.TestCase):
	def test_constructor(self):
		self.assertRaises(TypeError, Gradebook, [])
