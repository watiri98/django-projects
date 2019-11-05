
from django.test import TestCase
from .models import Teacher
from teacher.forms import TeacherForm
import datetime
from django.test import Client
from django.urls import reverse
class AddTeacherTestCase(TestCase):
    def setUp(self):
        self.data = {
        "first_name": "James",
        "last_name": "Mwai",
        "gender": "male",
        "email": "jmwai@gmail.com",
        "phone_number": "0752705000",
        "profession":"CTO",
        "date_joined":datetime.date.today(),
        "subject_training":"Python"
         }
        self.bad_data = {
        "first_name": 133,
        "last_name": "Mwai",
        "gender": "male",
        "email": "jmwai@gmail.com",
        "phone_number": "0752705000",
        "profession":"CTO",
        "subject_training":"Python",
        "date_joined":datetime.date.today(),
        }
    def test_teacher_form_accepts_valid_data(self):
        form = TeacherForm(self.data)
        self.assertFalse(form.is_valid())
    def test_teacher_form_rejects_invalid_data(self):
        form = TeacherForm(self.bad_data)
        self.assertFalse(form.is_valid())

    def test_add_teacher_view(self):
        client = Client()
        url = reverse("add_teacher")
        response = client.post(url,self.data)
        self.assertEqual(response.status_code,200)
        
    def test_add_teacher_view(self):
        client = Client()
        url = reverse("add_teacher")
        response = client.post(url,self.bad_data)
        self.assertEqual(response.status_code,400)
    

# Create your tests here.
