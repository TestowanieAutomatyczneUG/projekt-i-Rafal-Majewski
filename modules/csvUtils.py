from modules.Student import Student


def serializeStudent(student: Student) -> str:
	return f"{student.pesel};{student.firstName};{student.lastName}"


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
				file.write(
					f"{student.pesel};"
					f"{grade.teacher.pesel};"
					f"{grade.subject.id};"
					f"{grade.datetime};"
					f"{grade.value.name}\n"
				)
