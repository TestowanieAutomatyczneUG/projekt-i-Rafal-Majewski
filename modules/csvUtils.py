from modules.Student import Student
from modules.Grade import Grade
from modules.Subject import Subject
from modules.Teacher import Teacher
from modules.Gradebook import Gradebook


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


def exportStudents(students: frozenset[Student], filepath: str):
	with open(filepath, "w") as file:
		file.write("pesel;firstName;lastName\n")
		for student in students:
			file.write(serializeStudent(student) + "\n")


def exportStudentsGrades(students: frozenset[Student], filepath: str):
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


def exportSubjects(subjects: frozenset[Subject], filepath: str):
	with open(filepath, "w") as file:
		file.write("id;name\n")
		for subject in subjects:
			file.write(serializeSubject(subject) + "\n")


def exportTeachers(teachers: frozenset[Teacher], filepath: str):
	with open(filepath, "w") as file:
		file.write("pesel;firstName;lastName\n")
		for teacher in teachers:
			file.write(serializeTeacher(teacher) + "\n")


def exportTeacherSubjects(teacher: Teacher, filepath: str):
	with open(filepath, "w") as file:
		file.write("subjectId\n")
		for subject in teacher.subjects:
			file.write(f"{subject.id}\n")


def exportTeachersSubjects(teachers: frozenset[Teacher], filepath: str):
	with open(filepath, "w") as file:
		file.write("pesel;subjectId\n")
		for teacher in teachers:
			for subject in teacher.subjects:
				file.write(f"{teacher.pesel};{subject.id}\n")


def exportGradebook(gradebook: Gradebook, dirpath: str) -> None:
	exportStudents(gradebook.students, dirpath + "/students.csv")
	exportStudentsGrades(gradebook.students, dirpath + "/studentsGrades.csv")
	exportSubjects(gradebook.subjects, dirpath + "/subjects.csv")
	exportTeachers(gradebook.teachers, dirpath + "/teachers.csv")
	exportTeachersSubjects(gradebook.teachers, dirpath + "/teachersSubjects.csv")
