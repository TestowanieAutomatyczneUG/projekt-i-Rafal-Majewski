from modules.Person import Person
from abc import ABC


class PersonView(ABC):
	def __init__(self, person: Person) -> None:
		self.__person = person

	@property
	def person(self) -> Person:
		return self.__person
