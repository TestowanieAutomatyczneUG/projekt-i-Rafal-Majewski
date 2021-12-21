class Subject:
	def __init__(self, name: str) -> None:
		self.__name = name

	@property
	def name(self) -> str:
		return self.__name

	@name.setter
	def name(self, name: str) -> None:
		self.__name = name
