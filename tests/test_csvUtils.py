from modules.csvUtils import serializeStudent
import unittest
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
