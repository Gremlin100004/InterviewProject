from django.test import TestCase

class MainViewTests(TestCase):

    def test_url_undefined(self):
        """тестирование несуществующего адресса"""
        response = self.client.get('/undef/')
        self.assertEqual(response.status_code, 404)
