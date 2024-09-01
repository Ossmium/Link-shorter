from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('link_app.urls', 'link_app'), namespace='link_app')),
    path('', include(('accounts.urls', 'accounts'), namespace='accounts')),
]
