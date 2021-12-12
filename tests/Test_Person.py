import unittest
from modules.Person import Person


class Test_Person_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Person, [])

	def test_missing_lastName(self):
		with self.assertRaises(TypeError):
			Person(firstName="Jan")

	def test_missing_firstName(self):
		with self.assertRaises(TypeError):
			Person(lastName="Kowalski")


class Test_edit_Person(unittest.TestCase):
	def test_change_firstName(self):
		person = Person(firstName="Jan", lastName="Kowalski")
		person.firstName = "Adam"
		self.assertEqual(person.firstName, "Adam")

	def test_change_lastName(self):
		person = Person(firstName="Jan", lastName="Kowalski")
		person.lastName = "Nowak"
		self.assertEqual(person.lastName, "Nowak")
