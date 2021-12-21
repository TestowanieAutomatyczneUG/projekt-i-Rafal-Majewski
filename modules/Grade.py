from modules.Entry import Entry
from modules.Teacher import Teacher
from modules.Subject import Subject
from datetime import datetime as Datetime


class Grade(Entry):
	def __init__(
		self,
		*,
		subject: Subject,
		teacher: Teacher,
		value: str,
		datetime: Datetime
	) -> None:
		super().__init__(datetime=datetime)
		self.__subject = subject
		self.__teacher = teacher
		self.__value = value
