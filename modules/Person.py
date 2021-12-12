class Person:
	def __init__(self, *, firstName: str, lastName: str) -> None:
		self.firstName = firstName
		self.lastName = lastName

	@property
	def firstName(self) -> str:
		return self.__firstName

	@firstName.setter
	def firstName(self, firstName: str) -> None:
		self.__firstName = firstName

	@property
	def lastName(self) -> str:
		return self.__lastName

	@lastName.setter
	def lastName(self, lastName: str) -> None:
		self.__lastName = lastName
