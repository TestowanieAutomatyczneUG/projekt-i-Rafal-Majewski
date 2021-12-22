from modules.gradeStats import calculateTotalAverage, calculateAverageBySubject
from assertpy import assert_that  # type: ignore
from modules.Grade import Grade
from modules.Teacher import Teacher
from datetime import datetime as Datetime
from modules.Subject import Subject
from modules.GradeValue import GradeValue
import unittest


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
