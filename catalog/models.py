from django.db import models
from core.models import catalog, catalog_slug
from catalog.validators import validate_must_be_param
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import get_thumbnail, delete


class catalog_tag(catalog_slug):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


class catalog_category(catalog_slug):
    weight = models.PositiveSmallIntegerField(
        default=100,
        verbose_name="масса",
        help_text="минимум 0, максимум 32767"
    )

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "категории"


class catalog_item(catalog):
    text = models.TextField(
        validators=[validate_must_be_param('превосходно', 'роскошно')],
        verbose_name="описание",
        help_text="должно содержаться слово превосходно или роскошно"
    )
    category = models.ForeignKey(
        catalog_category(),
        on_delete=models.CASCADE,
        verbose_name="категория",
        help_text="выберете категорию"
    )
    tags = models.ManyToManyField(
        catalog_tag(),
        verbose_name="теги"
    )

    @property
    def get_img(self):
        return get_thumbnail(self.upload, '300x300', crop='center', quality=51)

    def img_tmb(self):
        if self.upload:
            return mark_safe(
                f'<img src="{self.get_img.url}">'
            )
        return 'нет изображений'

    img_tmb.short_description = 'фотогалерея'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name


class catalog_item_preview(models.Model):
    upload = models.ImageField('uploads/preview/%Y/%m')
    item = models.ForeignKey(
        catalog_item,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = "фотографии товара"
        verbose_name_plural = "фотогалерея товара"


class catalog_item_gallery(models.Model):
    upload = models.ImageField(upload_to='uploads/gallery/%Y/%m')
    tags = models.ManyToManyField(
        catalog_item(),
        verbose_name="товар"
    )

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = "фотографии товара"
        verbose_name_plural = "фотогалерея товара"
