import unittest
from modules.Entry import Entry
from datetime import datetime as Datetime


class Test_Entry_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Entry)

	def test_if_assigns_datetime(self):
		datetime = Datetime(year=2020, month=1, day=1)
		entry = Entry(datetime)
		self.assertEqual(entry.datetime, datetime)
