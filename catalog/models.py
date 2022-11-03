from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from catalog.validators import validate_must_be_param
from Core.models import catalog, catalog_slug


class catalog_tag(catalog_slug):
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class catalog_category(catalog_slug):
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
        validators=[validate_must_be_param('превосходно', 'роскошно')],
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
