from django.shortcuts import reverse
from django.test import TestCase

from feedback.forms import FormFeedback as ItemForm


class FormTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.form = ItemForm()

    def test_context(self):
        context = {'text': 'тест'}
        form = ItemForm(data=context)
        self.assertTrue(form.is_valid())

    def test_name_label(self):
        name_label = FormTests.form.fields['text'].label
        self.assertEquals(name_label, 'текст')

    def test_name_help_text(self):
        name_help_text = FormTests.form.fields['text'].help_text
        self.assertEquals(name_help_text, 'введите ваш текст')

    def test_redirect(self):
        response = self.client.post(
            reverse('feedback:feedback'),
            data={'text': 'тест'}
        )
        self.assertRedirects(response, reverse('feedback:feedback'))


# python manage.py test feedback
