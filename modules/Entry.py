from datetime import datetime as Datetime


class Entry:
	def __init__(self, datetime: Datetime) -> None:
		self.__datetime = datetime
