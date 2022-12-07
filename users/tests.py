from django.test import TestCase
from django.shortcuts import reverse


class ModelsTests(TestCase):
    def test_CreateEmployeeProfileView_context(self):
        response = self.client.get(reverse('catalog:item_list'))
        self.assertIn('birthday_users', response.context)
