from modules.Entry import Entry
from datetime import datetime as Datetime


class Comment(Entry):
	def __init__(self, *, datetime: Datetime, content: str) -> None:
		super().__init__(datetime=datetime)
		self.__content = content

	@property
	def content(self) -> str:
		return self.__content

	@content.setter
	def content(self, content: str) -> None:
		if not isinstance(content, str):
			raise TypeError("Content must be a string.")
		self.__content = content
