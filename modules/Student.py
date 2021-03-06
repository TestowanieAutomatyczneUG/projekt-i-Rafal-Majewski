from modules.Person import Person
from modules.Subject import Subject
from modules.Grade import Grade
from modules.Teacher import Teacher
from modules.Comment import Comment


def validateSubject(subject: Subject) -> None:
	if not isinstance(subject, Subject):
		raise TypeError("Subject must be a Subject object")


def validateGrade(grade: Grade) -> None:
	if not isinstance(grade, Grade):
		raise TypeError("Grade must be a Grade object")


def validateTeacher(teacher: Teacher) -> None:
	if not isinstance(teacher, Teacher):
		raise TypeError("Teacher must be a Teacher object")


def validateComment(comment: Comment) -> None:
	if not isinstance(comment, Comment):
		raise TypeError("Comment must be a Comment object")


class Student(Person):
	def __init__(
		self,
		*,
		firstName: str,
		lastName: str,
		pesel: str,
		subjects: set[Subject] = None,
		grades: set[Grade] = None,
		comments: set[Comment] = None
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
		self.__comments = set[Comment]()
		if comments is not None:
			for comment in comments:
				self.addComment(comment)

	def assignSubject(self, subject: Subject) -> Subject:
		validateSubject(subject)
		self.__subjects.add(subject)
		return subject

	def _unassignSubject(self, subject: Subject) -> Subject:
		if subject not in self.__subjects:
			raise ValueError("Subject is not assigned to this student")
		self.__subjects.remove(subject)
		return subject

	def unassignSubject(self, subject: Subject) -> Subject:
		validateSubject(subject)
		return self._unassignSubject(subject)

	@property
	def subjects(self) -> frozenset[Subject]:
		return frozenset(self.__subjects)

	def addGrade(self, grade: Grade) -> Grade:
		validateGrade(grade)
		self.__grades.add(grade)
		return grade

	def removeGrade(self, grade: Grade) -> Grade:
		validateGrade(grade)
		self.__grades.remove(grade)
		return grade

	@property
	def comments(self) -> frozenset[Comment]:
		return frozenset(self.__comments)

	def _addComment(self, comment: Comment) -> Comment:
		self.__comments.add(comment)
		return comment

	def addComment(self, comment: Comment) -> Comment:
		validateComment(comment)
		return self._addComment(comment)

	def _removeComment(self, comment: Comment) -> Comment:
		self.__comments.remove(comment)
		return comment

	def removeComment(self, comment: Comment) -> Comment:
		validateComment(comment)
		if comment not in self.__comments:
			raise ValueError("Comment is not assigned to this student")
		return self._removeComment(comment)

	@property
	def grades(self) -> frozenset[Grade]:
		return frozenset(self.__grades)

	def removeReferencesToTeacher(self, teacher: Teacher) -> None:
		validateTeacher(teacher)
		self.__grades = set([
			grade for grade in self.__grades if grade.teacher is not teacher
		])

	def removeReferencesToSubject(self, subject: Subject) -> Subject:
		validateSubject(subject)
		self.__grades = set([
			grade for grade in self.__grades if grade.subject is not subject
		])
		return self._unassignSubject(subject)

	def __eq__(self, other) -> bool:
		if not isinstance(other, Student):
			return False
		return (
			self.firstName == other.firstName
			and self.lastName == other.lastName
			and self.pesel == other.pesel
		)

	def __hash__(self) -> int:
		return hash(self.pesel)
