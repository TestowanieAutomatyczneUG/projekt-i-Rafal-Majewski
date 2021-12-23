from modules.Student import Student
from modules.Grade import Grade
from modules.Subject import Subject
from modules.Teacher import Teacher


def serializeStudent(student: Student) -> str:
	return f"{student.pesel};{student.firstName};{student.lastName}"


def deserializeStudent(studentString: str) -> Student:
	[pesel, firstName, lastName] = studentString.split(";")
	return Student(pesel=pesel, firstName=firstName, lastName=lastName)


def serializeGrade(grade: Grade) -> str:
	return (
		f"{grade.teacher.pesel};"
		f"{grade.subject.id};"
		f"{grade.datetime};"
		f"{grade.value.name}"
	)


def serializeSubject(subject: Subject) -> str:
	return f"{subject.id};{subject.name}"


def serializeTeacher(teacher: Teacher) -> str:
	return f"{teacher.pesel};{teacher.firstName};{teacher.lastName}"


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
