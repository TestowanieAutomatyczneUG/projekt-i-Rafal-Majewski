from modules.Person import Person
from modules.Subject import Subject
from modules.Grade import Grade
from modules.Teacher import Teacher


def validateSubject(subject: Subject) -> None:
	if not isinstance(subject, Subject):
		raise TypeError("Subject must be a Subject object")


class Student(Person):
	def __init__(
		self,
		*,
		firstName: str,
		lastName: str,
		pesel: str,
		subjects: set[Subject] = None,
		grades: set[Grade] = None,
	) -> None:
		super().__init__(firstName=firstName, lastName=lastName, pesel=pesel)
		self.__subjects = set[Subject]()
		if subjects is not None:
			for subject in subjects:
				self.assignSubject(subject)
		self.__grades = set[Grade]()
		if grades is not None:
			for grade in grades:
				self.addGrade(grade)

	def assignSubject(self, subject: Subject) -> Subject:
		validateSubject(subject)
		self.__subjects.add(subject)
		return subject

	def _unassignSubject(self, subject: Subject) -> Subject:
		self.__subjects.remove(subject)
		return subject

	def unassignSubject(self, subject: Subject) -> Subject:
		validateSubject(subject)
		return self._unassignSubject(subject)

	@property
	def subjects(self) -> frozenset[Subject]:
		return frozenset(self.__subjects)

	def addGrade(self, grade: Grade) -> Grade:
		self.__grades.add(grade)
		return grade

	def removeGrade(self, grade: Grade) -> Grade:
		self.__grades.remove(grade)
		return grade

	@property
	def grades(self) -> frozenset[Grade]:
		return frozenset(self.__grades)

	def removeReferencesToTeacher(self, teacher: Teacher) -> None:
		self.__grades = set([
			grade for grade in self.__grades if grade.teacher is not teacher
		])

	def removeReferencesToSubject(self, subject: Subject) -> Subject:
		self.__grades = set([
			grade for grade in self.__grades if grade.subject is not subject
		])
		return self._unassignSubject(subject)
