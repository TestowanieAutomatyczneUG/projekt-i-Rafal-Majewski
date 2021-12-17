from calendar import monthrange


def validatePesel(pesel: str):
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
	return True
