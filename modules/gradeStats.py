from typing import Optional
from modules.Grade import Grade
from modules.Subject import Subject


def calculateTotalAverage(grades: set[Grade]) -> Optional[float]:
	if len(grades) == 0:
		return None
	return sum(grade.value.value for grade in grades) / len(grades)


def calculateAverageBySubject(grades: set[Grade]) -> dict[Subject, float]:
	gradesBySubject = dict[Subject, set[Grade]]()
	for grade in grades:
		if grade.subject not in gradesBySubject:
			gradesBySubject[grade.subject] = set[Grade]()
		gradesBySubject[grade.subject].add(grade)
	return {
		subject: sum(grade.value.value for grade in grades) / len(grades)
		for subject, grades in gradesBySubject.items()
	}
