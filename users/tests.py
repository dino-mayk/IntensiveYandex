from datetime import date

from django.shortcuts import reverse
from django.test import Client, TestCase

from users.context_processors import get_birthday_user
from users.models import CustomUser


class ContextProcessorsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user = CustomUser.objects.create(
            email='test@gmail.com',
            password='123.,Abasd',
            birthday=str(date.today())
        )

    def tear_down():
        CustomUser.objects.delete()
        super().tearDown()

    def test_count_users(self):
        users_count = CustomUser.objects.count()
        self.assertEqual(CustomUser.objects.count(), users_count)

    def test_birthday_context(self):
        response = self.client.get(
            reverse('catalog:item_list')
        )
        self.assertIn('birthday_users', response.context)

    def test_get_birthday_user_positive(self):
        self.user.birthday = str(date.today())
        request = Client().get(
            reverse('catalog:item_list')
        )
        data = str(
            get_birthday_user(request)['birthday_users'][0].birthday
        )
        self.assertEqual(data, self.user.birthday)

    def test_get_birthday_user_negative(self):
        self.user.birthday = '2022-01-01'
        request = Client().get(
            reverse('catalog:item_list')
        )
        data = str(
            get_birthday_user(request)['birthday_users'][0].birthday
        )

        self.assertNotEqual(data, self.user.birthday)


# python manage.py test users
