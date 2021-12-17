def validatePesel(pesel: str):
	if len(pesel) != 11:
		return False
	if not pesel.isdigit():
		return False
	month = (int(pesel[2:4]) - 1) % 20 + 1
	if month > 12:
		return False
	return True
