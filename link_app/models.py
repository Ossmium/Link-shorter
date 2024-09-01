from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import random


class UserLinks(models.QuerySet):
    def user_links(self, user):
        return self.filter(user=user)


class Link(models.Model):
    full_url = models.URLField(
        max_length=2048,
        verbose_name='Полный URL',
    )
    short_url = models.CharField(
        max_length=settings.URL_LENGTH,
        unique=True,
        db_index=True,
        blank=True,
        verbose_name='Короткий URL'
    )
    click_count = models.IntegerField(
        default=0,
        verbose_name='Количество кликов'
    )
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата создания'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='links',
        verbose_name='Пользователь'
    )
    objects = UserLinks.as_manager()

    def save(self):
        if Link.objects.filter(full_url=self.full_url, user=self.user):
            raise ValueError('Вы уже добавляли данную ссылку')

        if not self.short_url:
            while True:
                self.short_url = ''.join(
                    random.choices(
                        settings.SYMBOLS,
                        k=settings.URL_LENGTH
                    )
                )
                if not Link.objects.filter(short_url=self.short_url).exists():
                    break
        super().save()

    def __str__(self) -> str:
        return self.full_url
