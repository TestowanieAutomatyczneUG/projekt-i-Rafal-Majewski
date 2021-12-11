class Gradebook:
	def __init__(self, *, schoolName: str) -> None:
		if not schoolName:
			raise ValueError("School name cannot be empty")
		self.schoolName = schoolName
