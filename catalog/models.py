from django.db import models
from django.db.models import Prefetch
from django.utils.safestring import mark_safe
from django_cleanup.signals import cleanup_pre_delete
from sorl.thumbnail import delete, get_thumbnail
from tinymce.models import HTMLField

from catalog.validators import validate_must_be_param
from core.models import catalog, catalog_slug


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


class ItemManager(models.Manager):
    def homepage(self):
        return (
            self.get_queryset()
                .filter(is_published=True, is_on_main=True)
                .select_related('category')
                .order_by('name')
                .prefetch_related(
                    Prefetch('tags', queryset=catalog_tag.objects.all())
                )
        )

    def catalog(self):
        return (
            self.get_queryset()
                .filter(is_published=True)
                .select_related('category')
                .order_by('category__name')
                .prefetch_related(
                    Prefetch('tags', queryset=catalog_tag.objects.all())
                )
        )


class catalog_item(catalog):
    text = HTMLField(
        validators=[validate_must_be_param('превосходно', 'роскошно')],
        verbose_name="описание",
        help_text="должно содержаться слово превосходно или роскошно"
    )
    objects = ItemManager()
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
    is_on_main = models.BooleanField(
        default=False,
        verbose_name="в главном"
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name


class catalog_item_preview(models.Model):
    upload = models.ImageField(
        upload_to='uploads/preview/%Y/%m',
        verbose_name="картинка",
        help_text='загрузите картинку'
    )
    item = models.OneToOneField(
        catalog_item,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="товар",
        help_text='выберете товар'
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

    img_tmb.short_description = 'превьюшки'
    img_tmb.allow_tags = True

    def sorl_delete(**kwargs):
        delete(kwargs['file'])

    cleanup_pre_delete.connect(sorl_delete)

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = "превью товара"
        verbose_name_plural = "превьюшки товаров"


class catalog_item_gallery(models.Model):
    upload = models.ImageField(
        upload_to='uploads/gallery/%Y/%m',
        verbose_name="картинка",
        help_text='загрузите картинку'
    )
    item = models.ForeignKey(
        catalog_item,
        on_delete=models.CASCADE,
        verbose_name="товар",
        help_text='выберете товар'
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

    def __str__(self):
        return self.upload.url

    class Meta:
        verbose_name = "фотографию товара"
        verbose_name_plural = "фотогалерея товаров"
