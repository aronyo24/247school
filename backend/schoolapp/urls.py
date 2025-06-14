

from django.contrib import admin
from django.urls import path

from . import views
from .views import  TeamList  # ✅ Add this line
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('api/teams/', TeamList.as_view()),

   # path('', views.home, name='home'),
    path('', views.subadmin_login, name='subadmin_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.subadmin_logout, name='subadmin_logout'),
    path('add-standard/', views.add_standard, name='add_standard'),
    path('add-subject/', views.add_subject, name='add_subject'),
    path('add-section/', views.add_section, name='add_section'),
    path('add-lesson/', views.add_lesson, name='add_lesson'),
    path('add-subsection/', views.add_subsection, name='add_subsection'),
    path('add-quiz/', views.add_quiz, name='add_quiz'),
    path('add-note/', views.add_note, name='add_note'),

]
from django.urls import path
from . import views


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
