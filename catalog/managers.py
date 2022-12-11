from django.db import models
from django.db.models import Prefetch

from core.models import catalog_slug


class catalog_tag(catalog_slug):
    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


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
