import unittest
from modules.Entry import Entry
from datetime import datetime as Datetime
from modules.Teacher import Teacher


class Test_Entry_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Entry)

	def test_if_assigns_datetime(self):
		datetime = Datetime(year=2020, month=1, day=1)
		entry = Entry(
			datetime=datetime,
			teacher=Teacher(
				firstName="Test",
				lastName="Test",
				pesel="85052342517",
			),
		)
		self.assertEqual(entry.datetime, datetime)

	def test_incorrect_datetime(self):
		datetime = "Jan 01 2020"
		with self.assertRaises(TypeError):
			Entry(
				datetime=datetime,
				teacher=Teacher(
					firstName="Test",
					lastName="Test",
					pesel="85052342517"
				)
			)

	def test_if_constructor_requires_named_datetime_argument(self):
		with self.assertRaises(TypeError):
			datetime = Datetime(year=2020, month=1, day=1)
			Entry(
				datetime,
				Teacher(
					firstName="Test",
					lastName="Test",
					pesel="85052342517",
				),
			)

	def test_incorrect_datetime_changed_manually(self):
		datetime = Datetime(year=2020, month=1, day=1)
		entry = Entry(
			datetime=datetime,
			teacher=Teacher(
				firstName="Test",
				lastName="Test",
				pesel="85052342517"
			),
		)
		with self.assertRaises(TypeError):
			entry.datetime = "Jan 01 2020"

	def test_incorrect_teacher_type(self):
		datetime = Datetime(year=2020, month=1, day=1)
		teacher = 1
		with self.assertRaises(TypeError):
			Entry(
				datetime=datetime,
				teacher=teacher,
			)
