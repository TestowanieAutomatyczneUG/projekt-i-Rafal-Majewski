from hamcrest.core.base_matcher import BaseMatcher
from calendar import monthrange


def _calculatePeselChecksum(peselPart: str):
	weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
	checksum = 10 - sum(
		weight * int(digit) for weight, digit in zip(weights, peselPart)
	) % 10
	return checksum


def _validatePesel(pesel: str):
	if len(pesel) != 11:
		return False
	if not pesel.isdigit():
		return False
	month = (int(pesel[2:4]) - 1) % 20 + 1
	if month > 12:
		return False
	year = int(pesel[0:2]) + {
		0: 1900,
		4: 1800,
		1: 2000,
		2: 2100,
		3: 2200
	}[int(pesel[2:4]) // 20]
	day = int(pesel[4:6])
	if day == 0 or day > monthrange(year, month)[1]:
		return False
	if _calculatePeselChecksum(pesel[:-1]) != int(pesel[-1]):
		return False
	return True


class ValidPesel(BaseMatcher):
	def _matches(self, value):
		return _validatePesel(value)

	def describe_to(self, description):
		description.append_text("valid pesel")


def valid_pesel():
	return ValidPesel()
