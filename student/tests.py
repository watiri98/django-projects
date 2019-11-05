from django.test import TestCase
from .models import Student
import datetime
from student.forms import StudentForm
from django.test import Client
from django.urls import reverse

# Create your tests here.
class StudentTestCase(TestCase):
    def setUp(self):
        self.student = Student(
            first_name = "Catherine",
            last_name ="Wanjiru",
            date_of_birth = datetime.date(1997,6,20),
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
        self.assertFalse(self.student.clean())

    def test_age_is_always_below_30(self):
        self.assertFalse(self.student.clean())

class AddstudentTestCase(TestCase):
    def setUp(self):
        self.data = {"first_name":"Catherine",
                     "last_name":"Wanjiru",
                     "date_of_birth":"datetime.date(1997,6,20)",
                     "gender":"female",
                     "registration_number":"2019",
                     "email":"watiricate16@gmail.com",
                     "phone_number" :"+25404660035",
                     "date_joined":"datetime.date.today()",
                    }
        self.bad_data = {"first_name":"Catherine",
                         "last_name":"Wanjiru",
                         "date_of_birth":"datetime.date(2000)",
                         "gender":"female",
                         "registration_number":"2019",
                         "email":"watiricate16@gmail.com",
                         "phone_number" :"+25404660035",
                         "date_joined":"datetime.date.today()",


                        }
    def test_student_form_accepts_valid_data(self):
        form = StudentForm(self.data)
        self.assertFalse(form.is_valid())
    def test_student_form_rejects_invalid_data(self):
        form = StudentForm(self.bad_data)
        self.assertFalse(form.is_valid())

    def test_add_student_view(self):
        client = Client()
        url = reverse("add_student")
        response = client.post(url,self.data)
        self.assertEqual(response.status_code,200)
        
    def test_add_student_view(self):
        client = Client()
        url = reverse("add_student")
        response = client.post(url,self.bad_data)
        self.assertEqual(response.status_code,400)

       



    
        

    

    # def test_get_age(self):
    #    self.assertIn(self.student.date_of_birth())



    
