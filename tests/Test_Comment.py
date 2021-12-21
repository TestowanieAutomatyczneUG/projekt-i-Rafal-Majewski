import unittest
from modules.Comment import Comment
from datetime import datetime as Datetime


class Test_Comment_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Comment)

	def test_if_sets_content(self):
		datetime = Datetime(year=2020, month=1, day=1)
		content = "Test content"
		comment = Comment(datetime=datetime, content=content)
		self.assertEqual(comment.content, content)
