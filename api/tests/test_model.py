from django.test import TestCase
from api import models

# Create your tests here.
class TestModel(TestCase): 
    def setUp(self): 
        self.instructor = {'name': 'test name', 'email':'test@gmail.com'}
        self.course = {'name':'test course', 'rating': 1, }


    def test_instructor(self):
     
        instructor_obj = models.Instructor.objects.create(**self.instructor)

        self.assertEqual(self.instructor['name'] , instructor_obj.name)
        self.assertEqual(self.instructor['email'] , instructor_obj.email)

        self.assertEqual(instructor_obj.get_name(), self.instructor['name'])
        self.assertEqual(instructor_obj.get_email(), self.instructor['email'])
    

    def test_course(self):
        instructor_obj = models.Instructor.objects.create(**self.instructor)
        course_obj = models.Course.objects.create(**self.course, instructor = instructor_obj)

        self.assertEqual(self.course['name'] , course_obj.name)
        self.assertEqual(self.course['rating'] , course_obj.rating)

        self.assertEqual(course_obj.get_name(), self.course['name'])
        self.assertEqual(course_obj.get_rating(), self.course['rating'])




