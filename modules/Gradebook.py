from modules.Student import Student
from modules.Teacher import Teacher
from modules.Subject import Subject


def validateStudentType(student: Student) -> None:
	if not isinstance(student, Student):
		raise TypeError("Student must be an instance of Student class.")


def validateTeacherType(teacher: Teacher) -> None:
	if not isinstance(teacher, Teacher):
		raise TypeError("Teacher must be an instance of Teacher class.")


def validateSubjectType(subject: Subject) -> None:
	if not isinstance(subject, Subject):
		raise TypeError("Subject must be an instance of Subject class.")


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
		validateStudentType(student)
		if student.pesel in self.__students:
			raise ValueError("Student with this PESEL already exists")
		self.__students[student.pesel] = student
		return student

	def addSubject(self, subject: Subject) -> Subject:
		validateSubjectType(subject)
		if subject.id in self.__subjects:
			raise ValueError("Subject with this ID already exists")
		self.__subjects[subject.id] = subject
		return subject

	def addTeacher(self, teacher: Teacher) -> Teacher:
		validateTeacherType(teacher)
		if teacher.pesel in self.__teachers:
			raise ValueError("Teacher with this PESEL already exists")
		self.__teachers[teacher.pesel] = teacher
		return teacher

	def removeStudent(self, student: Student) -> Student:
		validateStudentType(student)
		if student.pesel not in self.__students:
			raise ValueError("Student with this PESEL does not exist")
		del self.__students[student.pesel]
		return student

	def removeSubject(self, subject: Subject) -> Subject:
		validateSubjectType(subject)
		if subject.id not in self.__subjects:
			raise ValueError("Subject with this ID does not exist")
		del self.__subjects[subject.id]
		for teacher in self.__teachers.values():
			teacher.unassignSubject(subject)
		for student in self.__students.values():
			student.removeReferencesToSubject(subject)
		return subject

	def removeTeacher(self, teacher: Teacher) -> Teacher:
		validateTeacherType(teacher)
		if teacher.pesel not in self.__teachers:
			raise ValueError("Teacher with this PESEL does not exist")
		del self.__teachers[teacher.pesel]
		for student in self.__students.values():
			student.removeReferencesToTeacher(teacher)
		return teacher

	@property
	def students(self) -> frozenset[Student]:
		return frozenset(self.__students.values())

	@property
	def subjects(self) -> frozenset[Subject]:
		return frozenset(self.__subjects.values())

	@property
	def teachers(self) -> frozenset[Teacher]:
		return frozenset(self.__teachers.values())
