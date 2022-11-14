from django.db import models


class catalog(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name="опубликовано"
    )
    name = models.CharField(
        max_length=150,
        verbose_name="название",
        help_text="максимально 150 символов"
    )

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class catalog_slug(catalog):
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name="название для url",
        help_text="максимальная длина - 200 символов, \
            только цифры, буквы латиницы и символы - и _"
    )
