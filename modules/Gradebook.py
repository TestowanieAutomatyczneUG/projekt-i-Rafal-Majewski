from modules.Student import Student
from modules.Teacher import Teacher
from modules.Subject import Subject


class Gradebook:
	def __init__(self, *, schoolName: str) -> None:
		self.schoolName = schoolName
		self.__students = set[Student]()
		self.__teachers = set[Teacher]()
		self.__subjects = set[Subject]()

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

	def addStudent(self, *, firstName: str, lastName: str) -> Student:
		student = Student(firstName=firstName, lastName=lastName)
		self.__students.add(student)
		return student

	def addTeacher(self, *, firstName: str, lastName: str) -> Teacher:
		teacher = Teacher(firstName=firstName, lastName=lastName)
		self.__teachers.add(teacher)
		return teacher
