from django import forms
from content.models import a_standard, b_subject, c_section, d_lesson, e_subsection, f_quiz, g_note

class StandardForm(forms.ModelForm):
    class Meta:
        model = a_standard
        fields = ['name']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = b_subject
        fields = ['name', 'standard']

class SectionForm(forms.ModelForm):
    class Meta:
        model = c_section
        fields = ['name', 'subject']

class LessonForm(forms.ModelForm):
    class Meta:
        model = d_lesson
        fields = ['title', 'section', 'content_type']

class SubsectionForm(forms.ModelForm):
    class Meta:
        model = e_subsection
        fields = ['name', 'lesson', 'content', 'video_url']

class QuizForm(forms.ModelForm):
    class Meta:
        model = f_quiz
        fields = ['section', 'question', 'answer']

class NoteForm(forms.ModelForm):
    class Meta:
        model = g_note
        fields = ['title', 'section', 'file_type', 'file']