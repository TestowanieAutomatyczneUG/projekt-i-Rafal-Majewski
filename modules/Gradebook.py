from modules.Student import Student
from modules.Teacher import Teacher
from modules.Subject import Subject


class Gradebook:
	def __init__(
		self,
		*,
		schoolName: str,
		subjects: set[Subject] = None,
		students: set[Student] = None,
		teachers: set[Teacher] = None,
	) -> None:
		self.__subjects = dict[str, Subject]()
		self.__students = dict[str, Student]()
		self.__teachers = dict[str, Teacher]()
		if subjects is not None:
			for subject in subjects:
				self.addSubject(subject)
		if teachers is not None:
			for teacher in teachers:
				self.addTeacher(teacher)
		if students is not None:
			for student in students:
				self.addStudent(student)
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

	def addStudent(self, student: Student) -> Student:
		self.__students[student.pesel] = student
		return student

	def addSubject(self, subject: Subject) -> Subject:
		self.__subjects[subject.id] = subject
		return subject

	def addTeacher(self, teacher: Teacher) -> Teacher:
		self.__teachers[teacher.pesel] = teacher
		return teacher

	def removeStudent(self, student: Student) -> Student:
		del self.__students[student.pesel]
		return student

	@property
	def students(self) -> frozenset[Student]:
		return frozenset(self.__students.values())

	@property
	def subjects(self) -> frozenset[Subject]:
		return frozenset(self.__subjects.values())

	@property
	def teachers(self) -> frozenset[Teacher]:
		return frozenset(self.__teachers.values())
