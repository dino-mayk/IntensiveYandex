from django.db import models


class Feedback(models.Model):
    text = models.TextField(
        help_text="описание",
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="дата создания",
    )
