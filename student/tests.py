from django.test import TestCase
from .models import Student
import datetime

# Create your tests here.
class StudentTestCase(TestCase):
	def setUp(self):
		self.student = Student(
			first_name = "Catherine",
			last_name ="Wanjiru",
			date_of_birth = datetime.date(2012,6,20),
			gender = "female",
			registration_number = "2019",
			email = "watiricate16@gmail.com",
			phone_number = "+25404660035",
			date_joined = datetime.date.today(),
			)
	def test_full_name_contains_first_name(self):
		self.assertIn(self.student.first_name,self.student.full_name())
	def test_full_name_contains_last_name(self):
		self.assertIn(self.student.last_name,self.student.full_name())
	def test_age_is_always_above_17(self):
		self.assertFalse(self.student.clean() < 17)

	def test_age_is_always_below_30(self):
		self.assertFalse(self.student.clean() > 30)

	

    # def test_get_age(self):
   	#    self.assertIn(self.student.date_of_birth())



	
