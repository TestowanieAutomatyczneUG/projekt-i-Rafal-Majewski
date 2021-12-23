from modules.Student import Student
from modules.Grade import Grade


def serializeStudent(student: Student) -> str:
	return f"{student.pesel};{student.firstName};{student.lastName}"


def serializeGrade(grade: Grade) -> str:
	return (
		f"{grade.teacher.pesel};"
		f"{grade.subject.id};"
		f"{grade.datetime};"
		f"{grade.value.name}"
	)


def exportStudents(students: set[Student], filepath: str):
	with open(filepath, "w") as file:
		file.write("pesel;firstName;lastName\n")
		for student in students:
			file.write(serializeStudent(student) + "\n")


def exportStudentsGrades(students: set[Student], filepath: str):
	with open(filepath, "w") as file:
		file.write("studentPesel;teacherPesel;subjectId;datetime;value\n")
		for student in students:
			for grade in student.grades:
				file.write(f"{student.pesel};" + serializeGrade(grade) + "\n")


def exportStudentGrades(student: Student, filepath: str):
	with open(filepath, "w") as file:
		file.write("teacherPesel;subjectId;datetime;value\n")
		for grade in student.grades:
			file.write(serializeGrade(grade) + "\n")
