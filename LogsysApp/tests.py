from django.test import  TestCase
from django.contrib.auth.forms import User



class LogsysAppViewTests(TestCase):

    def setUp(self):
        User.objects.create_user(username='username', password='password')

    def test_login(self):
        """тестирование авторизации пользователя"""
        response = self.client.post('/auth/login/', {'username': "username", 'password' : "password"})
        self.assertEqual(response.status_code, 302)
        response2 = self.client.post('/auth/login/', {'username': "undef", 'password': "undef"})
        self.assertEqual(response2.status_code, 200)

    def test_logout(self):
        """тестирование выхода авторизированого пользователя"""
        self.client.login(username='username', password='password')
        response = self.client.get('/auth/logout/')
        self.assertEqual(response.status_code, 302)

    def test_registration(self):
        """тестирование регистрации пользователя"""
        response = self.client.get('/auth/register/')
        self.assertEqual(response.status_code, 302) # проверка что это не POST запрос
        response = self.client.post('/auth/register/', {'username': "usernametest", 'password': "passwordtest1",
                                                        'password2': "passwordtest"})
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/auth/register/', {'username': "usernametest", 'password': "pas",
                                                        'password2': "pas"})
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/auth/register/', {'username': "usernametest", 'password': "usernametest",
                                                        'password2': "usernametest"})
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/auth/register/', {'username': "username", 'password': "passwordtest",
                                                        'password2': "passwordtest"})
        self.assertEqual(response.status_code, 200)
        response = self.client.post('/auth/register/', {'username': "usernametest", 'password': "passwordtest", 'password2': "passwordtest"})
        self.assertEqual(response.status_code, 200) # проверка на регистрацию
        response = self.client.post('/auth/login/', {'username': "usernametest", 'password': "passwordtest"})
        self.assertEqual(response.status_code, 302) # проверка пользователя которого зарегистрировали