import json
from django.test import TestCase, Client
from django.urls import reverse
import os

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.course_url = reverse('course')
        self.register_url = reverse('register')
        self.welcome_url = reverse('welcome')
        self.create_course_url = reverse('create_course')
        self.create_forum_url = reverse('create_forum')
        self.sync_data_url = reverse('sync_data')
        self.login_url = reverse('login')

    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_course_view(self):
        response = self.client.get(self.course_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'course.html')

    def test_register_view(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_welcome_view(self):
        response = self.client.get(self.welcome_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'welcome.html')

    def test_create_course_view(self):
        response = self.client.get(self.create_course_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crear_curso.html')

    def test_create_forum_view(self):
        response = self.client.get(self.create_forum_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'crear_foro.html')

    def test_sync_data_view(self):
        response = self.client.get(self.sync_data_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')


    def test_reg_course_view(self):
        course_data = {
            'name': 'Django for Beginners',
            'description': 'Learn Django web development from scratch',
            'price': 50.0
        }
        response = self.client.post(reverse('reg_course'), json.dumps(course_data), content_type='application/json')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/home/')
        # check that the course file was created
        course_id = response.url.split('/')[-2]
        course_file = f"data/courses/{course_id}.json"
        self.assertTrue(os.path.exists(course_file))

    def test_reg_forum_view(self):
        forum_data = {
            'name': 'General Discussion',
            'description': 'Discuss anything related to Django'
        }
