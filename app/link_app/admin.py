from django.contrib import admin
from .models import Link


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        'full_url',
        'short_url',
        'click_count',
        'created_at',
        'user'
    )
