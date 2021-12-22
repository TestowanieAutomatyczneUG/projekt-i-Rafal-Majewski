import unittest
from modules.PersonView import PersonView
from modules.Person import Person


class Test_constructor(unittest.TestCase):
	def test_person_property(self):
		person = Person(firstName="Jan", lastName="Kowalski", pesel="85052342517")
		personView = PersonView(person)
		self.assertIs(personView.person, person)
