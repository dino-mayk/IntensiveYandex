from django.db import models


class catalog(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name="Идентификатор"
    )
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
