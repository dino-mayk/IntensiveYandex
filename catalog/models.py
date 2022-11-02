from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# validate_slug
from catalog.validators import validate_amazing
from Core.models import catalog


class catalog_tag(catalog):
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name="Название для url",
        help_text="максимальная длина - 200 символов, \
            только цифры, буквы латиницы и символы - и _"
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class catalog_category(catalog):
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name="Название для url",
        help_text="максимальная длина - 200 символов, \
            только цифры, буквы латиницы и символы - и _"
    )
    weight = models.PositiveIntegerField(
        default=100,
        validators=[MinValueValidator(1), MaxValueValidator(32766)],
        verbose_name="Масса",
        help_text="Минимум 1, максимум 32766"
    )

    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"


class catalog_item(catalog):
    text = models.TextField(
        validators=[validate_amazing],
        verbose_name="Описание",
        help_text="Должно содержаться слово превосходно или роскошно"
    )
    category = models.ForeignKey(
        catalog_category(),
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Выберете категорию"
    )
    tags = models.ManyToManyField(
        catalog_tag(),
        verbose_name="Теги"
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
