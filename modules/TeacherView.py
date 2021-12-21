from modules.PersonView import PersonView
from modules.Teacher import Teacher
from modules.Student import Student
from modules.Grade import Grade


class TeacherView(PersonView):
	def __init__(self, teacher: Teacher) -> None:
		super().__init__(teacher)
		self.__teacher = teacher

	def giveGrade(self, student: Student, grade: Grade) -> Grade:
		if grade.subject not in student.subjects:
			raise ValueError("Subject is not assigned to student.")
		if grade.subject not in self.__teacher.subjects:
			raise ValueError("Subject is not assigned to teacher.")
		return student.addGrade(grade)

	def takeGrade(self, student: Student, grade: Grade) -> Grade:
		return student.removeGrade(grade)
