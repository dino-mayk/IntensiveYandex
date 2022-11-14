from django.test import Client, TestCase
from django.core.exceptions import ValidationError
from .models import catalog_item as Item
from .models import catalog_category as Category
from .models import catalog_tag as Tag


class StaticURLTests(TestCase):
    def test_item_list_endpoint(self):
        with self.subTest('there is a catalog'):
            response = Client().get('/catalog/')
            self.assertEqual(response.status_code, 200)

    def test_item_detail_endpoint(self):
        tests = [
            {
                'value': 1,
                'description': 'positive number',
                'code': 200
            },
            {
                'value': 202,
                'description': 'positive number',
                'code': 200
            },
            {
                'value': 0,
                'description': 'zero',
                'code': 404
            },
            {
                'value': -1,
                'description': 'negative number',
                'code': 404
            },
            {
                'value': -101,
                'description': 'negative number',
                'code': 404
            },
            {
                'value': 1.0,
                'description': 'float number',
                'code': 404
            },
            {
                'value': 1.205,
                'description': 'float number',
                'code': 404
            },
            {
                'value': -1.0,
                'description': 'negative float number',
                'code': 404
            },
            {
                'value': -1.205,
                'description': 'negative float number',
                'code': 404
            },
            {
                'value': '01',
                'description': 'string',
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
            name="тест",
            slug="test_test-testA1",
            weight=32766
        )
        cls.tag = Tag.objects.create(
            name="тест",
            slug="test_test-testA2"
        )

    def tear_down():
        Item.objects.delete()
        super().tearDown()

    def test_item_positive(self):
        item_count = Item.objects.count()

        self.item = Item(
            name="тест",
            text="роскОшно",
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
            slug="test_test-testA3",
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
            name="тест",
            slug="test_test-testA4"
        )
        self.tag.full_clean()
        self.tag.save()

        self.assertEqual(Tag.objects.count(), tag_count + 1)

    def test_tag_negative(self):
        tag_count = Tag.objects.count()

        with self.assertRaises(ValidationError):
            self.tag = Tag(
                name="тест",
                slug="test_test-testI234#%&рп"
            )
            self.tag.full_clean()
            self.tag.save()

        self.assertEqual(Tag.objects.count(), tag_count)
