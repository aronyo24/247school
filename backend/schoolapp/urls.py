

from django.contrib import admin
from django.urls import path
from .views import  TeamList  # ✅ Add this line
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('api/teams/', TeamList.as_view()),  # << test endpoint
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
