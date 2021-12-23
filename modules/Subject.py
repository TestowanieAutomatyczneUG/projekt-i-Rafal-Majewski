class Subject:
	def __init__(self, id: str, name: str) -> None:
		self.__id = id
		self.name = name

	@property
	def name(self) -> str:
		return self.__name

	@name.setter
	def name(self, name: str) -> None:
		if not isinstance(name, str):
			raise TypeError("Name must be a string")
		self.__name = name

	@property
	def id(self) -> str:
		return self.__id
