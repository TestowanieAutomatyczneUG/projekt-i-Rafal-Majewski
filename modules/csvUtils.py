from modules.Student import Student


def serializeStudent(student: Student) -> str:
	return f"{student.pesel};{student.firstName};{student.lastName}"


def exportStudents(students: set[Student], filepath: str):
	with open(filepath, "w") as file:
		file.write("pesel;firstName;lastName\n")
		for student in students:
			file.write(serializeStudent(student) + "\n")
