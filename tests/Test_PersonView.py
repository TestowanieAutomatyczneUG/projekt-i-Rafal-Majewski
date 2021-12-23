import pytest
from modules.PersonView import PersonView
from modules.Person import Person


def test_person_property():
	person = Person(firstName="Jan", lastName="Kowalski", pesel="85052342517")
	personView = PersonView(person)
	assert personView.person is person


def test_person_of_wrong_type():
	with pytest.raises(TypeError):
		PersonView(3)
