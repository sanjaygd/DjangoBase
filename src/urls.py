from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from decouple import config

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('src.apps.accounts.urls'), name='accounts'),
]

DEBUG_TOOLBAR = config("DEBUG_TOOLBAR", default=False, cast=bool)

if settings.DEBUG  and DEBUG_TOOLBAR:
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
