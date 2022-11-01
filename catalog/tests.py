from django.test import Client, TestCase
from django.core.exceptions import ValidationError
from .models import catalog_item as Item
from .models import catalog_category as Category
from .models import catalog_tag as Tag


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


class ModelsTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.category = Category.objects.create(
            name="Тест",
            slug="test_test-testI234",
            weight=32766
        )
        cls.tag = Tag.objects.create(
            name="Тест",
            slug="test_test-testI234"
        )

    def test_item_positive(self):
        item_count = Item.objects.count()

        self.item = Item(
            name="тест",
            text="РоскОшно",
            category=self.category
        )
        self.item.save()
        self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count + 1)

    def test_item_negative(self):
        item_count = Item.objects.count()

        with self.assertRaises(ValidationError):
            self.item = Item(
                name="тест",
                text="ошибка",
                category=self.category
            )
            self.item.full_clean()
            self.item.save()
            self.item.tags.add(self.tag)

        self.assertEqual(Item.objects.count(), item_count)

    def test_category_positive(self):
        category_count = Category.objects.count()

        self.category = Category(
            name="тест",
            slug="test_test-testI24",
            weight=32766
        )
        self.category.full_clean()
        self.category.save()

        self.assertEqual(Category.objects.count(), category_count + 1)

    def test_category_negative(self):
        category_count = Category.objects.count()

        with self.assertRaises(ValidationError):
            self.category = Category(
                name="тест",
                slug="test_test-testI234#%&рп",
                weight=-1
            )
            self.category.full_clean()
            self.category.save()

        self.assertEqual(Category.objects.count(), category_count)

    def test_tag_positive(self):
        tag_count = Tag.objects.count()

        self.tag = Tag(
            name="тестик",
            slug="test_test-testI23"
        )
        self.tag.full_clean()
        self.tag.save()

        self.assertEqual(Tag.objects.count(), tag_count + 1)

    def test_tag_negative(self):
        tag_count = Tag.objects.count()

        with self.assertRaises(ValidationError):
            self.tag = Tag(
                name="тестик",
                slug="test_test-testI23#%&рп"
            )
            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(Tag.objects.count(), tag_count)
