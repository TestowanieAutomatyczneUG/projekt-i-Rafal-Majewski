from modules.Entry import Entry
from modules.Teacher import Teacher
from modules.Subject import Subject
from datetime import datetime as Datetime
from modules.GradeValue import GradeValue


class Grade(Entry):
	def __init__(
		self,
		*,
		subject: Subject,
		teacher: Teacher,
		value: GradeValue,
		datetime: Datetime,
	) -> None:
		super().__init__(datetime=datetime, teacher=teacher)
		self.subject = subject
		self.value = value

	@property
	def subject(self) -> Subject:
		return self.__subject

	@subject.setter
	def subject(self, subject: Subject) -> None:
		if not isinstance(subject, Subject):
			raise TypeError("Subject must be an instance of Subject class.")
		self.__subject = subject

	@property
	def value(self) -> GradeValue:
		return self.__value

	@value.setter
	def value(self, value: GradeValue) -> None:
		if not isinstance(value, GradeValue):
			raise TypeError("Value must be an instance of GradeValue class.")
		self.__value = value
