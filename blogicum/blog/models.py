from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class PublishedCreatedModel(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Добавлено',
        help_text='Если установить дату и время в будущем — можно делать отложенные публикации.'
    )

    class Meta:
        abstract = True

class Location(PublishedCreatedModel):
    name = models.CharField(
        max_length=256,
        verbose_name='Местоположение'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'



class Post(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
