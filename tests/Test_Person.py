import unittest
from modules.Person import Person


class Test_Person_constructor(unittest.TestCase):
	def test_no_arguments(self):
		self.assertRaises(TypeError, Person, [])

	def test_only_firstName(self):
		with self.assertRaises(TypeError):
			Person(firstName="Jan")

	def test_onlyLastName(self):
		with self.assertRaises(TypeError):
			Person(lastName="Kowalski")

	def test_incorrect_pesel(self):
		with self.assertRaises(ValueError):
			Person(firstName="Jan", lastName="Kowalski", pesel="85052342518")

	def test_pesel_getter(self):
		person = Person(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		self.assertEqual(person.pesel, "85052342517")

	def test_firstName_of_wrong_type(self):
		with self.assertRaises(TypeError):
			Person(firstName=53, lastName="Kowalski", pesel="85052342517")

	def test_empty_firstName(self):
		with self.assertRaises(ValueError):
			Person(firstName="", lastName="Kowalski", pesel="85052342517")


class Test_edit_Person(unittest.TestCase):
	def test_change_firstName(self):
		person = Person(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		person.firstName = "Adam"
		self.assertEqual(person.firstName, "Adam")

	def test_change_lastName(self):
		person = Person(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		person.lastName = "Nowak"
		self.assertEqual(person.lastName, "Nowak")

	def test_change_pesel(self):
		person = Person(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		person.pesel = "93101341329"
		self.assertEqual(person.pesel, "93101341329")
