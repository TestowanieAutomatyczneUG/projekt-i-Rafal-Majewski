from modules.PersonView import PersonView
from modules.Gradebook import Gradebook
from modules.Teacher import Teacher


class TeacherView(PersonView):
	def __init__(self, gradebook: Gradebook, teacher: Teacher) -> None:
		super().__init__(gradebook, teacher)
