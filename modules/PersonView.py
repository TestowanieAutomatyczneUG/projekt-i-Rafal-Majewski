from modules.Person import Person
from abc import ABC


class PersonView(ABC):
	def __init__(self, person: Person) -> None:
		if not isinstance(person, Person):
			raise TypeError("Person must be a Person object")
		self.__person = person

	@property
	def person(self) -> Person:
		return self.__person
