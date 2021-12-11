from modules.Gradebook import Gradebook
import unittest


class Test_Gradebook(unittest.TestCase):
	def test_constructor(self):
		self.assertRaises(TypeError, Gradebook, [])
