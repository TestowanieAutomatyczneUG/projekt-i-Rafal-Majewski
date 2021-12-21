from modules.Person import Person
from modules.Subject import Subject


class Teacher(Person):
	def __init__(
		self,
		*,
		firstName: str,
		lastName: str,
		pesel: str,
		subjects: set[Subject] = None
	) -> None:
		self.__subjects = set[Subject]()
		if subjects is not None:
			for subject in subjects:
				self.addSubject(subject)
		super().__init__(firstName=firstName, lastName=lastName, pesel=pesel)

	@property
	def subjects(self) -> frozenset[Subject]:
		return frozenset(self.__subjects)

	def addSubject(self, subject: Subject) -> Subject:
		self.__subjects.add(subject)
		return subject

	def unassignSubject(self, subject: Subject) -> Subject:
		self.__subjects.remove(subject)
		return subject
