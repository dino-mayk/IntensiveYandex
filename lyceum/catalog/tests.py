from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_item_list_endpoint(self):
        response = Client().get('/catalog/')
        self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint_int(self):
        response = Client().get('/catalog/1/')
        self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint_str(self):
        response = Client().get('/catalog/hello/')
        self.assertEqual(response.status_code, 404)
