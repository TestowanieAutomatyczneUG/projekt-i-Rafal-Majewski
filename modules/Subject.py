class Subject:
	def __init__(self, name: str) -> None:
		self.name = name

	@property
	def name(self) -> str:
		return self.__name

	@name.setter
	def name(self, name: str) -> None:
		if not isinstance(name, str):
			raise TypeError("Name must be a string")
		self.__name = name
