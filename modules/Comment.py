from modules.Entry import Entry
from datetime import datetime as Datetime
from modules.Teacher import Teacher


class Comment(Entry):
	def __init__(
		self,
		*,
		datetime: Datetime,
		content: str,
		teacher: Teacher
	) -> None:
		super().__init__(datetime=datetime, teacher=teacher)
		self.content = content

	@property
	def content(self) -> str:
		return self.__content

	@content.setter
	def content(self, content: str) -> None:
		if not isinstance(content, str):
			raise TypeError("Content must be a string.")
		self.__content = content
