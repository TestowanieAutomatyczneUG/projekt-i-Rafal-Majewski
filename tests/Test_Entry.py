import unittest
from modules.Entry import Entry


class Test_Entry_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Entry)
