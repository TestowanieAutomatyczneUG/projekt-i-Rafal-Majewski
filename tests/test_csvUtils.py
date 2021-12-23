from modules.csvUtils import serializeStudent, exportStudents
import unittest
import unittest.mock
from modules.Student import Student
from parameterized import parameterized_class  # type: ignore


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
