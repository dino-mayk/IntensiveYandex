from django.db import models

from catalog.models import catalog_item as Item
from users.models import CustomUser


class Mark(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="пользователь",
        help_text='выберете пользователя'
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        verbose_name="товар",
        help_text='выберете товар'
    )
    RATING = [
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь'),
    ]
    mark = models.PositiveSmallIntegerField(
        verbose_name='ваша оценка:',
        choices=RATING,
    )

    def __str__(self):
        return f'оценка  товара {self.item.name} \
            пользователем {self.user.email}'

    class Meta:
        verbose_name = 'Оценку'
        verbose_name_plural = 'Оценки'
        unique_together = ('user', 'item',)
