from modules.Person import Person
from modules.Gradebook import Gradebook
from abc import ABC


class PersonView(ABC):
	def __init__(self, gradebook: Gradebook, person: Person) -> None:
		pass
