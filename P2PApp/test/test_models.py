import os
import json
import shutil
from django.test import TestCase
from django.conf import settings
from P2PApp.models import cargar_datos_json, load_courses, load_profile, check_courses, copy_export_file

class TestUtils(TestCase):
    def setUp(self):
        self.datos = {'users': [{'name': 'John', 'age': 30}, {'name': 'Jane', 'age': 25}], 'courses': [{'name': 'Math', 'code': 'MTH101'}, {'name': 'Science', 'code': 'SCI101'}]}
        self.datos_json = json.dumps(self.datos)
        self.test_path = os.path.join(settings.BASE_DIR, 'test')
        self.course_file = os.path.join(settings.BASE_DIR, 'data/courses/test.json')

    def tearDown(self):
        if os.path.exists(self.test_path):
            shutil.rmtree(self.test_path)
        if os.path.exists(self.course_file):
            os.remove(self.course_file)


        datos = cargar_datos_json()
        self.assertEqual(datos, self.datos)

    def test_load_courses(self):
        course_data = {'name': 'Test Course', 'code': 'TST101'}
        with open(self.course_file, 'w') as f:
            f.write(json.dumps(course_data))

        courses = load_courses()
        self.assertEqual(len(courses), 1)
        self.assertIn('test', courses)
        self.assertEqual(courses['test'], course_data)

    def test_load_profile(self):
        user_data = {'name': 'Test User', 'email': 'test@example.com'}
        user_file = os.path.join(settings.BASE_DIR, 'data/user.json')
        with open(user_file, 'w') as f:
            f.write(json.dumps(user_data))

        profile = load_profile()
        self.assertIsNotNone(profile)
        self.assertEqual(profile, user_data)

    def test_check_courses(self):
        course_data = {'name': 'Test Course', 'code': 'TST101'}
        with open(self.course_file, 'w') as f:
            f.write(json.dumps(course_data))

        self.assertTrue(check_courses('test'))


        copy_export_file(src_file, dst_file)
        self.assertTrue(os.path.exists(dst_file))

        with open(dst_file, 'r') as f:
            data = f.read()

        self.assertEqual(data, self.datos_json)