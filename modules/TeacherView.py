from modules.PersonView import PersonView
from modules.Teacher import Teacher
from modules.Student import Student
from modules.Grade import Grade
from modules.Comment import Comment


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
		if grade.subject not in student.subjects:
			raise ValueError("Subject is not assigned to student.")
		if grade.subject not in self.__teacher.subjects:
			raise ValueError("Subject is not assigned to teacher.")
		return student.removeGrade(grade)

	def giveComment(self, student: Student, comment: Comment) -> Comment:
		if not isinstance(comment, Comment):
			raise TypeError("Comment must be a Comment object")
		if comment.teacher is not self.__teacher:
			raise ValueError("Comment is not assigned to this teacher.")
		return student._addComment(comment)

	def takeComment(self, student: Student, comment: Comment) -> Comment:
		if not isinstance(comment, Comment):
			raise TypeError("Comment must be a Comment object")
		if comment.teacher is not self.__teacher:
			raise ValueError("Comment is not assigned to this teacher.")
		return student._removeComment(comment)
