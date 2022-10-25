from django.test import Client, TestCase


# https://www.caktusgroup.com/blog/2017/05/29/subtests-are-best/
# https://django.fun/ru/docs/django/4.1/topics/http/urls/#path-converters


class StaticURLTests(TestCase):
    def test_item_list_endpoint(self):
        with self.subTest('There is a catalog.'):
            response = Client().get('/catalog/')
            self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint_int(self):
        with self.subTest('There is a catalog with positive numbers.'):
            response = Client().get('/catalog/1/')
            self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint_zero_int(self):
        with self.subTest('No catalog with zero.'):
            response = Client().get('/catalog/0/')
            self.assertEqual(response.status_code, 404)

    def test_item_detail_endpoint_negative_int(self):
        with self.subTest('No catalog with negative numbers.'):
            response = Client().get('/catalog/-1/')
            self.assertEqual(response.status_code, 404)

    def test_item_detail_endpoint_float(self):
        with self.subTest('No catalog with float numbers.'):
            response = Client().get('/catalog/1.1/')
            self.assertEqual(response.status_code, 404)

    def test_item_detail_endpoint_negative_float(self):
        with self.subTest('No catalog with negative float numbers.'):
            response = Client().get('/catalog/-1.1/')
            self.assertEqual(response.status_code, 404)

    def test_item_detail_endpoint_str(self):
        with self.subTest('No catalog with strings.'):
            response = Client().get('/catalog/hello/')
            self.assertEqual(response.status_code, 404)
