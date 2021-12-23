from modules.csvUtils import \
	serializeStudent, \
	exportStudents, \
	exportStudentsGrades, \
	exportStudentGrades, \
	deserializeStudent
import unittest
import unittest.mock
from modules.Student import Student
from parameterized import parameterized_class, parameterized  # type: ignore
from modules.Subject import Subject
from modules.Teacher import Teacher
from modules.GradeValue import GradeValue
from modules.Grade import Grade
from datetime import datetime as Datetime


@parameterized_class(
	("student", "expectedString"),
	[
		(
			Student(pesel="76072443188", firstName="Jan", lastName="Kowalski"),
			"76072443188;Jan;Kowalski"
		),
		(
			Student(pesel="86110298656", firstName="Adam", lastName="Nowak"),
			"86110298656;Adam;Nowak"
		),
		(
			Student(pesel="05320732334", firstName="Anna", lastName="Kowalska"),
			"05320732334;Anna;Kowalska"
		),
		(
			Student(pesel="02231887245", firstName="Janina", lastName="Nowak"),
			"02231887245;Janina;Nowak"
		),
		(
			Student(pesel="59081097474", firstName="Krzysztof", lastName="Kowalski"),
			"59081097474;Krzysztof;Kowalski"
		),
	]
)
class Test_serializeStudent(unittest.TestCase):
	def test_correct(self):
		self.assertEqual(serializeStudent(self.student), self.expectedString)


class Test_deserializeStudent(unittest.TestCase):
	@parameterized.expand(
		[
			(
				"76072443188;Jan;Kowalski",
				Student(pesel="76072443188", firstName="Jan", lastName="Kowalski")
			),
			(
				"86110298656;Adam;Nowak",
				Student(pesel="86110298656", firstName="Adam", lastName="Nowak")
			),
			(
				"05320732334;Anna;Kowalska",
				Student(pesel="05320732334", firstName="Anna", lastName="Kowalska")
			),
		]
	)
	def test_correct(self, studentString: str, expectedStudent: Student):
		self.assertEqual(deserializeStudent(studentString), expectedStudent)


class Test_exportStudents(unittest.TestCase):
	def test_correct_if_opens(self):
		students = [
			Student(pesel="76072443188", firstName="Jan", lastName="Kowalski"),
			Student(pesel="86110298656", firstName="Adam", lastName="Nowak"),
			Student(pesel="05320732334", firstName="Anna", lastName="Kowalska"),
		]
		with unittest.mock.patch("builtins.open") as mockOpen:
			exportStudents(students, "test.csv")
		mockOpen.assert_called_once_with("test.csv", "w")

	def test_correct_if_writes_header(self):
		students = [
			Student(pesel="76072443188", firstName="Jan", lastName="Kowalski"),
			Student(pesel="86110298656", firstName="Adam", lastName="Nowak"),
			Student(pesel="05320732334", firstName="Anna", lastName="Kowalska"),
		]
		with unittest.mock.patch("builtins.open") as mockOpen:
			exportStudents(students, "test.csv")
		mockOpen.return_value.__enter__.return_value.write.assert_any_call(
			"pesel;firstName;lastName\n"
		)

	def test_correct_if_writes_students(self):
		students = [
			Student(pesel="76072443188", firstName="Jan", lastName="Kowalski"),
			Student(pesel="86110298656", firstName="Adam", lastName="Nowak"),
			Student(pesel="05320732334", firstName="Anna", lastName="Kowalska"),
		]
		with unittest.mock.patch("builtins.open") as mockOpen:
			exportStudents(students, "test.csv")
		mockOpen.return_value.__enter__.return_value.write.assert_has_calls(
			[
				unittest.mock.call("pesel;firstName;lastName\n"),
				unittest.mock.call("76072443188;Jan;Kowalski\n"),
				unittest.mock.call("86110298656;Adam;Nowak\n"),
				unittest.mock.call("05320732334;Anna;Kowalska\n"),
			],
			any_order=True
		)

	def test_if_header_at_the_top(self):
		students = [
			Student(pesel="76072443188", firstName="Jan", lastName="Kowalski"),
		]
		with unittest.mock.patch("builtins.open") as mockOpen:
			exportStudents(students, "test.csv")
		mockOpen.return_value.__enter__.return_value.write.assert_has_calls(
			[
				unittest.mock.call("pesel;firstName;lastName\n"),
				unittest.mock.call("76072443188;Jan;Kowalski\n"),
			],
		)


class Test_exportStudentsGrades(unittest.TestCase):
	def test_correct_if_opens(self):
		subject = Subject(name="Matematyka", id="math")
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="76072443188")
		students = [
			Student(
				pesel="76072443188",
				firstName="Jan",
				lastName="Kowalski",
				grades=[
					Grade(
						subject=subject,
						teacher=teacher,
						value=GradeValue.G2,
						datetime=Datetime(2020, 1, 1)
					),
				],
			),
			Student(
				pesel="86110298656",
				firstName="Adam",
				lastName="Nowak",
				grades=[
					Grade(
						subject=subject,
						teacher=teacher,
						value=GradeValue.G3PLUS,
						datetime=Datetime(2020, 12, 13)
					),
					Grade(
						subject=subject,
						teacher=teacher,
						value=GradeValue.G6,
						datetime=Datetime(2019, 3, 13)
					),
				],
			),
		]
		with unittest.mock.patch("builtins.open") as mockOpen:
			exportStudentsGrades(students, "test.csv")
		mockOpen.assert_called_once_with("test.csv", "w")

	def test_correct_if_writes_header(self):
		subject = Subject(name="Matematyka", id="math")
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="85032929358")
		students = [
			Student(
				pesel="76072443188",
				firstName="Jan",
				lastName="Kowalski",
				grades=[
					Grade(
						subject=subject,
						teacher=teacher,
						value=GradeValue.G2,
						datetime=Datetime(2020, 1, 1)
					),
				],
			),
			Student(
				pesel="86110298656",
				firstName="Adam",
				lastName="Nowak",
				grades=[
					Grade(
						subject=subject,
						teacher=teacher,
						value=GradeValue.G3PLUS,
						datetime=Datetime(2020, 12, 13)
					),
					Grade(
						subject=subject,
						teacher=teacher,
						value=GradeValue.G6,
						datetime=Datetime(2019, 3, 13)
					),
				],
			),
		]
		with unittest.mock.patch("builtins.open") as mockOpen:
			exportStudentsGrades(students, "test.csv")
		mockOpen.return_value.__enter__.return_value.write.assert_any_call(
			"studentPesel;teacherPesel;subjectId;datetime;value\n"
		)

	def test_correct_if_writes_grades(self):
		subject = Subject(name="Matematyka", id="math")
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="76072443188")
		students = [
			Student(
				pesel="76072443188",
				firstName="Jan",
				lastName="Kowalski",
				grades=[
					Grade(
						subject=subject,
						teacher=teacher,
						value=GradeValue.G2,
						datetime=Datetime(2020, 1, 1)
					),
				],
			),
			Student(
				pesel="86110298656",
				firstName="Adam",
				lastName="Nowak",
				grades=[
					Grade(
						subject=subject,
						teacher=teacher,
						value=GradeValue.G3PLUS,
						datetime=Datetime(2020, 12, 13)
					),
					Grade(
						subject=subject,
						teacher=teacher,
						value=GradeValue.G6,
						datetime=Datetime(2019, 3, 13)
					),
				],
			),
		]
		with unittest.mock.patch("builtins.open") as mockOpen:
			exportStudentsGrades(students, "test.csv")
		mockOpen.return_value.__enter__.return_value.write.assert_has_calls(
			[
				unittest.mock.call(
					"76072443188;76072443188;math;2020-01-01 00:00:00;G2\n"
				),
				unittest.mock.call(
					"86110298656;76072443188;math;2019-03-13 00:00:00;G6\n"
				),
				unittest.mock.call(
					"86110298656;76072443188;math;2020-12-13 00:00:00;G3PLUS\n"
				),
				unittest.mock.call(
					"studentPesel;teacherPesel;subjectId;datetime;value\n"
				),
			],
			any_order=True,
		)


class Test_exportStudentGrades(unittest.TestCase):
	def test_correct_if_opens(self):
		subject = Subject(name="Matematyka", id="math")
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="76072443188")
		student = Student(
			pesel="76072443188",
			firstName="Jan",
			lastName="Kowalski",
			grades=[
				Grade(
					subject=subject,
					teacher=teacher,
					value=GradeValue.G2,
					datetime=Datetime(2020, 1, 1)
				),
			],
		)
		with unittest.mock.patch("builtins.open") as mockOpen:
			exportStudentGrades(student, "test.csv")
		mockOpen.assert_called_once_with("test.csv", "w")

	def test_correct_if_writes_header(self):
		subject = Subject(name="Matematyka", id="math")
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="76072443188")
		student = Student(
			pesel="76072443188",
			firstName="Jan",
			lastName="Kowalski",
			grades=[
				Grade(
					subject=subject,
					teacher=teacher,
					value=GradeValue.G2,
					datetime=Datetime(2020, 1, 1)
				),
			],
		)
		with unittest.mock.patch("builtins.open") as mockOpen:
			exportStudentGrades(student, "test.csv")
		mockOpen.return_value.__enter__.return_value.write.assert_any_call(
			"teacherPesel;subjectId;datetime;value\n"
		)

	def test_correct_if_writes_grades(self):
		subject = Subject(name="Matematyka", id="math")
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="76072443188")
		student = Student(
			pesel="76072443188",
			firstName="Jan",
			lastName="Kowalski",
			grades=[
				Grade(
					subject=subject,
					teacher=teacher,
					value=GradeValue.G2,
					datetime=Datetime(2020, 1, 1)
				),
			],
		)
		with unittest.mock.patch("builtins.open") as mockOpen:
			exportStudentGrades(student, "test.csv")
		mockOpen.return_value.__enter__.return_value.write.assert_has_calls(
			[
				unittest.mock.call(
					"76072443188;math;2020-01-01 00:00:00;G2\n"
				),
				unittest.mock.call(
					"teacherPesel;subjectId;datetime;value\n"
				),
			],
			any_order=True,
		)
