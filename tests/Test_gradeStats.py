from modules.gradeStats import totalAverage
from assertpy import assert_that  # type: ignore
from modules.Grade import Grade


class Test_totalAverage:
	def test_empty(self):
		assert_that(totalAverage(set[Grade]())).is_none()
