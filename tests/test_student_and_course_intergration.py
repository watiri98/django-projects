from django.test import TestCase
from student.models import Student
from course.models import Course
import datetime
class  StudentCourseTestCase(TestCase):
	def setUp(self):
		self.student_a = Student.objects.create(
			first_name = "Catherine",
			last_name ="Wanjiru",
			date_of_birth = datetime.date(1997,6,20),
			gender = "female",
			registration_number = "2019",
			email = "watiricate16@gmail.com",
			phone_number = "+25404660035",
			date_joined = datetime.date.today(),
			)
		self.student_b = Student.objects.create(
			first_name = "Clarence",
			last_name ="Anyango",
			date_of_birth = datetime.date(1992,10,16),
			gender = "male",
			registration_number = "2012",
			email = "clarean@gmail.com",
			phone_number = "+2543678235",
			date_joined = datetime.date.today(),

			)
		self.python = Course.objects.create(
			name = "Python",
			duration_in_months = 9,
			start_date = datetime.date(2019,2,2),
			end_date = datetime.date(2019,11,30),
			description = "Backend programming language",
			)
		self.javascript = Course.objects.create(
			name = "Javascript",
			duration_in_months = 9,
			start_date = datetime.date(2019,2,2),
			end_date = datetime.date(2019,11,30),
			description = "Frontend stuff",
			)
		self.design = Course.objects.create(
			name = "Graphic",
			duration_in_months = 9,
			start_date = datetime.date(2019,2,2),
			end_date = datetime.date(2019,11,30),
			description = "Visual representation of information",)
	def test_student_can_join_a_course(self):
		
		self.student_a.courses.add(self.python,)
		self.assertEqual(self.student_a.courses.count(),1)
		self.student_a.courses.add(self.javascript,)
		self.assertEqual(self.student_a.courses.count(),2)
		self.student_a.courses.add(self.design,)
		self.assertEqual(self.student_a.courses.count(),3)

	
	def test_student_can_join_many_courses(self):
		# student = self.student_a.save()
		# student_a.courses.add(self.python)
		self.student_b.courses.add(self.python,self.javascript,self.design)
		self.assertEqual(self.student_b.courses.count(),3)

		

	
	