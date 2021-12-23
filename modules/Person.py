from modules.utils import validatePesel
from abc import ABC


class Person(ABC):
	def __init__(self, *, firstName: str, lastName: str, pesel: str) -> None:
		self.firstName = firstName
		self.lastName = lastName
		self.pesel = pesel

	@property
	def firstName(self) -> str:
		return self.__firstName

	@firstName.setter
	def firstName(self, firstName: str) -> None:
		if not isinstance(firstName, str):
			raise TypeError("First name must be a string")
		if not firstName:
			raise ValueError("First name cannot be empty")
		self.__firstName = firstName

	@property
	def lastName(self) -> str:
		return self.__lastName

	@lastName.setter
	def lastName(self, lastName: str) -> None:
		if not isinstance(lastName, str):
			raise TypeError("Last name must be a string")
		if not lastName:
			raise ValueError("Last name cannot be empty")
		self.__lastName = lastName

	@property
	def pesel(self) -> str:
		return self.__pesel

	@pesel.setter
	def pesel(self, pesel: str) -> None:
		if not validatePesel(pesel):
			raise ValueError("Invalid PESEL")
		self.__pesel = pesel
