from datetime import datetime as Datetime


class Entry:
	def __init__(self, datetime: Datetime) -> None:
		self.datetime = datetime

	@property
	def datetime(self) -> Datetime:
		return self.__datetime

	@datetime.setter
	def datetime(self, datetime: Datetime) -> None:
		self.__datetime = datetime
