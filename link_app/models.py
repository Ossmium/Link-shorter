from django.db import models
from django.contrib.auth.models import User


class Link(models.Model):
    full_url = models.URLField(unique=True)
    short_url = models.CharField(
        max_length=6,
        unique=True,
        db_index=True,
        blank=True
    )
    click_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self):
        if not self.short_url:
            while True:
                self.short_url = ''.join()

    def __str__(self) -> str:
        return self.full_url
