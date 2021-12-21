from modules.Person import Person
from abc import ABC


class PersonView(ABC):
	def __init__(self, person: Person) -> None:
		pass
