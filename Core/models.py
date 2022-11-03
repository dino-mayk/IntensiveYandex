from django.db import models
from django.core.validators import RegexValidator


class catalog(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="Название",
        help_text="Максимально 150 символов"
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class catalog_slug(catalog):
    slug = models.SlugField(
        validators=[
            RegexValidator(regex='^[a-zA-Z0-9]+(?:[_|-][a-zA-Z0-9]+)*$')
        ],
        max_length=200,
        unique=True,
        verbose_name="Название для url",
        help_text="максимальная длина - 200 символов, \
            только цифры, буквы латиницы и символы - и _"
    )
