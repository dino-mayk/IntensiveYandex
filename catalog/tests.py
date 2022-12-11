from django.core.exceptions import ValidationError
from django.test import TestCase

from catalog.models import catalog_category as Category
from catalog.models import catalog_item as Item
from catalog.models import catalog_tag as Tag


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


# python manage.py test catalog
