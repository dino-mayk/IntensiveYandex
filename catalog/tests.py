from django.test import Client, TestCase


class StaticURLTests(TestCase):
    def test_item_list_endpoint(self):
        with self.subTest('There is a catalog'):
            response = Client().get('/catalog/')
            self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint(self):
        tests = [
            {
                'value': 1,
                'description': 'Positive number',
                'code': 200
            },
            {
                'value': 202,
                'description': 'Positive number',
                'code': 200
            },
            {
                'value': 0,
                'description': 'Zero',
                'code': 404
            },
            {
                'value': -1,
                'description': 'Negative number',
                'code': 404
            },
            {
                'value': -101,
                'description': 'Negative number',
                'code': 404
            },
            {
                'value': 1.0,
                'description': 'Float number',
                'code': 404
            },
            {
                'value': 1.205,
                'description': 'Float number',
                'code': 404
            },
            {
                'value': -1.0,
                'description':
                'Negative float number',
                'code': 404
            },
            {
                'value': -1.205,
                'description': 'Negative float number',
                'code': 404
            },
            {
                'value': '01',
                'description': 'String',
                'code': 404
            }
        ]

        for dictionary in tests:
            value = str(dictionary['value'])
            description = str(dictionary['description'])
            code = int(dictionary['code'])

            with self.subTest(description):
                response = Client().get(f'/catalog/{value}/')
                self.assertEqual(response.status_code, code)
