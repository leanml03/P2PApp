from django.test import SimpleTestCase
from django.urls import reverse, resolve
from P2PApp.views import *

class TestUrls(SimpleTestCase):

    def test_guardar_json_url_resolves(self):
        url = reverse('guardar-json')
        self.assertEquals(resolve(url).func, guardar_json)

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_create_course_url_resolves(self):
        url = reverse('create_course')
        self.assertEquals(resolve(url).func, create_course)

    def test_reg_course_url_resolves(self):
        url = reverse('reg_course')
        self.assertEquals(resolve(url).func, reg_course)

    def test_sync_data_url_resolves(self):
        url = reverse('sync_data')
        self.assertEquals(resolve(url).func, sync_data)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def test_invalid_url_resolves(self):
        url = reverse('invalid')
        self.assertEquals(resolve(url).func, InvalidData)

    def test_loginloaded_url_resolves(self):
        url = reverse('loginloaded')
        self.assertEquals(resolve(url).func, loginloaded)

    def test_exportUser_url_resolves(self):
        url = reverse('exportUser')
        self.assertEquals(resolve(url).func, exportUser)

    def test_exportCourse_url_resolves(self):
        url = reverse('exportCourse')
        self.assertEquals(resolve(url).func, exportCourse)

    def test_reg_forum_url_resolves(self):
        url = reverse('reg_forum')
        self.assertEquals(resolve(url).func, reg_forum)

    def test_course_url_resolves(self):
        url = reverse('course')
        self.assertEquals(resolve(url).func, course)

    def test_create_forum_url_resolves(self):
        url = reverse('create_forum')
        self.assertEquals(resolve(url).func, create_forum)