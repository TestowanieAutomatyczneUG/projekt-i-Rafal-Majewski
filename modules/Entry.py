from datetime import datetime as Datetime
from abc import ABC
from modules.Teacher import Teacher


class Entry(ABC):
	def __init__(self, *, datetime: Datetime, teacher: Teacher) -> None:
		self.datetime = datetime
		self.__teacher = teacher

	@property
	def datetime(self) -> Datetime:
		return self.__datetime

	@datetime.setter
	def datetime(self, datetime: Datetime) -> None:
		if not isinstance(datetime, Datetime):
			raise TypeError("Datetime must be an instance of Datetime class.")
		self.__datetime = datetime

	@property
	def teacher(self) -> Teacher:
		return self.__teacher
