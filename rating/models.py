from django.db import models

from catalog.models import catalog_item as Item
from users.models import CustomUser


class Mark(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,
                             verbose_name='Пользователь',
                             )
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             verbose_name='Товар',
                             )

    RATING = [
        (1, 'Ненависть'),
        (2, 'Неприязнь'),
        (3, 'Нейтрально'),
        (4, 'Обожание'),
        (5, 'Любовь'),
    ]
    mark = models.IntegerField(verbose_name='Оценка',
                               choices=RATING,
                               )

    def __str__(self):
        return f'Оценка  товара {self.item.name} пользователем {self.user.email}'

    class Meta:
        verbose_name = 'Оценку'
        verbose_name_plural = 'Оценки'
