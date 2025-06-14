

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import TeamList, TrackVisitorView
urlpatterns = [

    path('api/teams/', TeamList.as_view()),
    path("api/track-visitor/", TrackVisitorView.as_view()),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
