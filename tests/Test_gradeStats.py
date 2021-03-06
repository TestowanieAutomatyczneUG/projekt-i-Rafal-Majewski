from modules.gradeStats import calculateTotalAverage, calculateAverageBySubject
from assertpy import assert_that, add_extension  # type: ignore
from modules.Grade import Grade
from modules.Teacher import Teacher
from datetime import datetime as Datetime
from modules.Subject import Subject
from modules.GradeValue import GradeValue
import unittest


def is_dict_close_to(self, otherDict: dict, tolerance: float):
	if not isinstance(self.val, dict):
		self.error(f"{self.val} is not a dict")
	if not isinstance(otherDict, dict):
		self.error(f"{otherDict} is not a dict")
	if self.val.keys() != otherDict.keys():
		self.error(f"{self.val} and {otherDict} have different keys")
	for key in self.val.keys():
		assert_that(self.val[key]).is_close_to(otherDict[key], tolerance=tolerance)


add_extension(is_dict_close_to)


class Test_totalAverage(unittest.TestCase):
	def test_empty(self):
		assert_that(calculateTotalAverage(set[Grade]())).is_none()

	def test_one(self):
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="86110298656")
		subject = Subject(id="1", name="Matematyka")
		grades = set[Grade]([
			Grade(
				teacher=teacher,
				value=GradeValue.G2,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject
			),
		])
		assert_that(calculateTotalAverage(grades)).is_close_to(2.0, tolerance=0.001)

	def test_three(self):
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="86110298656")
		subject = Subject(id="1", name="Matematyka")
		grades = set[Grade]([
			Grade(
				teacher=teacher,
				value=GradeValue.G2PLUS,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject
			),
			Grade(
				teacher=teacher,
				value=GradeValue.G2,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject
			),
			Grade(
				teacher=teacher,
				value=GradeValue.G5MINUS,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject
			),
		])
		assert_that(calculateTotalAverage(grades)).is_close_to(3.0, tolerance=0.001)


class Test_calculateAverageBySubject(unittest.TestCase):
	def test_empty(self):
		assert_that(calculateAverageBySubject(set[Grade]())).is_equal_to({})

	def test_four_check_subjects(self):
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="86110298656")
		subject1 = Subject(id="1", name="Matematyka")
		subject2 = Subject(id="2", name="Fizyka")
		grades = set[Grade]([
			Grade(
				teacher=teacher,
				value=GradeValue.G2PLUS,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject1
			),
			Grade(
				teacher=teacher,
				value=GradeValue.G2,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject1
			),
			Grade(
				teacher=teacher,
				value=GradeValue.G5MINUS,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject2
			),
			Grade(
				teacher=teacher,
				value=GradeValue.G3,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject2
			),
		])
		assert_that(calculateAverageBySubject(grades)).contains_only(
			subject1,
			subject2
		)

	def test_four(self):
		teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="86110298656")
		subject1 = Subject(id="1", name="Matematyka")
		subject2 = Subject(id="2", name="Fizyka")
		grades = set[Grade]([
			Grade(
				teacher=teacher,
				value=GradeValue.G2PLUS,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject1
			),
			Grade(
				teacher=teacher,
				value=GradeValue.G2,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject1
			),
			Grade(
				teacher=teacher,
				value=GradeValue.G5MINUS,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject2
			),
			Grade(
				teacher=teacher,
				value=GradeValue.G3,
				datetime=Datetime(year=2020, month=1, day=1),
				subject=subject2
			),
		])
		assert_that(calculateAverageBySubject(grades)).is_dict_close_to(
			dict([
				(subject1, 2.125),
				(subject2, 3.875),
			]),
			tolerance=0.001
		)
