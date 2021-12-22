import unittest
from modules.Comment import Comment
from datetime import datetime as Datetime
from assertpy import assert_that  # type: ignore
from modules.Teacher import Teacher


class Test_Comment_constructor(unittest.TestCase):
	def test_no_arguments(self):
		assert_that(Comment).raises(TypeError).when_called_with()

	def test_if_sets_content(self):
		datetime = Datetime(year=2020, month=1, day=1)
		content = "Test content"
		comment = Comment(
			datetime=datetime,
			content=content,
			teacher=Teacher(
				firstName="Test", lastName="Test", pesel="85052342517"
			)
		)
		assert_that(comment.content).is_equal_to(content)

	def test_wrong_content_type(self):
		datetime = Datetime(year=2020, month=1, day=1)
		content = 1
		assert_that(Comment).raises(TypeError).when_called_with(
			datetime=datetime,
			content=content,
			teacher=Teacher(
				firstName="Test",
				lastName="Test",
				pesel="85052342517"
			)
		)
