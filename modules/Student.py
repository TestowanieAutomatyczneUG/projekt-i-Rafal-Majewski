from modules.Person import Person
from modules.Subject import Subject


class Student(Person):
	def __init__(
		self,
		*,
		firstName: str,
		lastName: str,
		subjects: set[Subject] = None
	) -> None:
		super().__init__(firstName=firstName, lastName=lastName)
		self.__subjects = set[Subject]() if subjects is None else subjects

	def assignSubject(self, subject: Subject) -> None:
		self.__subjects.add(subject)

	@property
	def subjects(self) -> frozenset[Subject]:
		return frozenset(self.__subjects)
