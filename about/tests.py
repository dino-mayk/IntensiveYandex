from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        with self.subTest('there is a about.'):
            response = Client().get('/about/')
            self.assertEqual(response.status_code, 200)
