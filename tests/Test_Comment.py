import unittest
from modules.Comment import Comment


class Test_Comment_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Comment)
