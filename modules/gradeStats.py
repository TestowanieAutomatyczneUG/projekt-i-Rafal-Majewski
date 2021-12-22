from typing import Optional
from modules.Grade import Grade


def calculateTotalAverage(grades: set[Grade]) -> Optional[float]:
	if len(grades) == 0:
		return None
	return sum(grade.value.value for grade in grades) / len(grades)
