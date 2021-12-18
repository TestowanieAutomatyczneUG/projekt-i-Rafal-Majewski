from calendar import monthrange


def _calculatePeselChecksum(peselPart: str):
	weighths = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
	checksum = 10 - sum(
		weight * int(digit) for weight, digit in zip(weighths, peselPart)
	) % 10
	return checksum


def calculatePeselChecksum(peselPart: str):
	if not isinstance(peselPart, str):
		raise TypeError("Pesel part must be a string.")
	if not peselPart.isdigit():
		raise ValueError("Pesel part must be a string of digits.")
	if len(peselPart) != 10:
		raise ValueError("Pesel part must be 10 characters long.")
	return _calculatePeselChecksum(peselPart)


def validatePesel(pesel: str):
	"""
	Validates a PESEL number according to
	https://en.wikipedia.org/wiki/PESEL#Format.

	>>> validatePesel("95092971213")
	True
	>>> validatePesel("95173378812")
	False
	>>> validatePesel("9509297")
	False
	"""
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


if __name__ == "__main__":
	import doctest
	import sys
	if doctest.testmod().failed:
		sys.exit(1)
