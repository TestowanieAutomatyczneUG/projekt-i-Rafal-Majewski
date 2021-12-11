class Gradebook:
	def __init__(self, *, schoolName: str) -> None:
		self.schoolName = schoolName

	@property
	def schoolName(self) -> str:
		return self.__schoolName

	@schoolName.setter
	def schoolName(self, schoolName: str) -> None:
		if not isinstance(schoolName, str):
			raise TypeError("School name must be a string")
		if not schoolName:
			raise ValueError("School name cannot be empty")
		self.__schoolName = schoolName
