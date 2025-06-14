from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.urls import reverse
from django.apps import apps
from django.contrib.admin import site
from django.urls.exceptions import NoReverseMatch
from rest_framework.generics import ListAPIView
from team.models import TeamMember
from .serializers import TeamMemberSerializer

from django.shortcuts import render, redirect
from content.models import a_standard, b_subject, c_section, d_lesson, e_subsection, f_quiz, g_note
from content.forms import (
    StandardForm, SubjectForm, SectionForm, LessonForm,
    SubsectionForm, QuizForm, NoteForm
)

def add_standard(request):
    if request.method == 'POST':
        form = StandardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('standard_list')  # Replace with your list view
    else:
        form = StandardForm()
    return render(request, 'add_standard.html', {'form': form})

def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')  # Replace with your list view
    else:
        form = SubjectForm()
    return render(request, 'add_subject.html', {'form': form})

def add_section(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')  # Replace with your list view
    else:
        form = SectionForm()
    return render(request, 'add_section.html', {'form': form})

def add_lesson(request):
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lesson_list')  # Replace with your list view
    else:
        form = LessonForm()
    return render(request, 'add_lesson.html', {'form': form})

def add_subsection(request):
    if request.method == 'POST':
        form = SubsectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subsection_list')  # Replace with your list view
    else:
        form = SubsectionForm()
    return render(request, 'add_subsection.html', {'form': form})

def add_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('quiz_list')  # Replace with your list view
    else:
        form = QuizForm()
    return render(request, 'add_quiz.html', {'form': form})

def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('note_list')  # Replace with your list view
    else:
        form = NoteForm()
    return render(request, 'add_note.html', {'form': form})
# Helper function to check if a user is a subadmin
def is_subadmin(user):
    return user.is_staff  # You can replace this with custom permission checks


# Function to get a list of apps and models for the subadmin
def get_subadmin_apps(user):
    app_list = []

    for app_config in apps.get_app_configs():
        models = []

        for model in app_config.get_models():
            opts = model._meta
            can_view = user.has_perm(f"{opts.app_label}.view_{opts.model_name}")
            can_add = user.has_perm(f"{opts.app_label}.add_{opts.model_name}")

            # Check if the model is registered with the admin site
            if model in site._registry:
                try:
                    list_url = reverse(f'admin:{opts.app_label}_{opts.model_name}_changelist') if can_view else None
                    add_url = reverse(f'admin:{opts.app_label}_{opts.model_name}_add') if can_add else None
                except NoReverseMatch:
                    # Skip models without changelist or add URLs
                    continue

                if can_view or can_add:
                    models.append({
                        'object_name': opts.object_name,
                        'name': opts.verbose_name_plural.title(),
                        'list_url': list_url,
                        'add_url': add_url,
                    })

        if models:
            app_list.append({
                'name': app_config.verbose_name.title(),
                'models': models,
            })

    return app_list


# Dashboard view for subadmins
@login_required(login_url="/subadmin/login/")
@user_passes_test(is_subadmin)
def dashboard(request):
    context = {
        'dashboard_name': 'School247 Admin',
        'subadmin_apps': get_subadmin_apps(request.user),
    }
    return render(request, "dashboard.html", context)


# Subadmin login view
def subadmin_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and is_subadmin(user):
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials or not authorized.")
    return render(request, "login.html")


# Subadmin logout view
def subadmin_logout(request):
    logout(request)
    return redirect("subadmin_login")


# API view for listing team members
class TeamList(ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer