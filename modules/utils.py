def validatePesel(pesel: str):
	if len(pesel) != 11:
		return False
	if not pesel.isdigit():
		return False
	return True
