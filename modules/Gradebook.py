from modules.Student import Student
from modules.Teacher import Teacher
from modules.Subject import Subject


class Gradebook:
	def __init__(self, *, schoolName: str, subjects: set[Subject] = None) -> None:
		self.schoolName = schoolName
		self.__students = set[Student]()
		self.__teachers = set[Teacher]()
		self.__subjects = set[Subject]() if subjects is None else subjects

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

	def addStudent(self, student: Student) -> Student:
		self.__students.add(student)
		return student

	def addTeacher(self, teacher: Teacher) -> Teacher:
		self.__teachers.add(teacher)
		return teacher

	def removeStudent(self, student: Student) -> Student:
		self.__students.remove(student)
		return student

	@property
	def students(self) -> frozenset[Student]:
		return frozenset(self.__students)

	@property
	def subjects(self) -> frozenset[Subject]:
		return frozenset(self.__subjects)
