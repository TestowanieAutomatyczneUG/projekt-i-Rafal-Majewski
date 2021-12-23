import pytest
from modules.Grade import Grade
from modules.Subject import Subject
from modules.Teacher import Teacher
from modules.GradeValue import GradeValue
from datetime import datetime as Datetime


def test_no_arguments():
	with pytest.raises(TypeError):
		Grade()


def test_correct():
	subject = Subject(id="test", name="Math")
	teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517")
	datetime = Datetime(year=2020, month=1, day=1)
	Grade(
		subject=subject,
		teacher=teacher,
		value=GradeValue.G3PLUS,
		datetime=datetime
	)
	assert True


def test_teacher_property():
	teacher = Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517")
	grade = Grade(
		subject=Subject(id="test", name="Math"),
		teacher=teacher,
		value=GradeValue.G3PLUS,
		datetime=Datetime(year=2020, month=1, day=1)
	)
	assert grade.teacher is teacher


def test_incorrect_subject_type():
	with pytest.raises(TypeError):
		Grade(
			subject=1,
			teacher=Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517"),
			value=GradeValue.G3PLUS,
			datetime=Datetime(year=2020, month=1, day=1)
		)


def test_incorrect_value_type():
	with pytest.raises(TypeError):
		Grade(
			subject=Subject(id="test", name="Math"),
			teacher=Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517"),
			value=1,
			datetime=Datetime(year=2020, month=1, day=1)
		)


def test_value_property():
	grade = Grade(
		subject=Subject(id="test", name="Math"),
		teacher=Teacher(firstName="Jan", lastName="Kowalski", pesel="85052342517"),
		value=GradeValue.G3PLUS,
		datetime=Datetime(year=2020, month=1, day=1)
	)
	assert grade.value is GradeValue.G3PLUS
