from modules.Person import Person
from modules.Subject import Subject


class Student(Person):
	def __init__(
		self,
		*,
		firstName: str,
		lastName: str,
		pesel: str,
		subjects: set[Subject] = None
	) -> None:
		super().__init__(firstName=firstName, lastName=lastName, pesel=pesel)
		self.__subjects = set[Subject]()
		if subjects is not None:
			for subject in subjects:
				self.assignSubject(subject)

	def assignSubject(self, subject: Subject) -> Subject:
		if not isinstance(subject, Subject):
			raise TypeError("Subject must be an instance of Subject class.")
		self.__subjects.add(subject)
		return subject

	def unassignSubject(self, subject: Subject) -> Subject:
		if not isinstance(subject, Subject):
			raise TypeError("Subject must be an instance of Subject class.")
		self.__subjects.remove(subject)
		return subject

	@property
	def subjects(self) -> frozenset[Subject]:
		return frozenset(self.__subjects)
