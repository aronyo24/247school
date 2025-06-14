from django.contrib import admin
from .models import a_standard, b_subject, c_section, d_lesson, e_subsection, f_quiz, g_note

# Subsection inline inside Lesson
class SubsectionInline(admin.TabularInline):
    model = e_subsection
    extra = 1

# Quiz inline inside Section
class QuizInline(admin.TabularInline):
    model = f_quiz
    extra = 1

# Note inline inside Section
class NoteInline(admin.TabularInline):
    model = g_note
    extra = 1

# Subject inline inside Standard
class SubjectInline(admin.TabularInline):
    model = b_subject
    extra = 1

# Section inline inside Subject
class SectionInline(admin.TabularInline):
    model = c_section
    extra = 1

# Lesson inline inside Section
class LessonInline(admin.TabularInline):
    model = d_lesson
    extra = 1

# Final Admin Classes with full nesting:

@admin.register(a_standard)
class StandardAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [SubjectInline]  # Nested Subjects inside Standard

@admin.register(b_subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'standard')
    list_filter = ('standard',)
    search_fields = ('name', 'standard__name')
    inlines = [SectionInline]  # Nested Sections inside Subject

@admin.register(c_section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    list_filter = ('subject__standard', 'subject')
    search_fields = ('name', 'subject__name')
    inlines = [LessonInline, QuizInline, NoteInline]  # Nested Lessons, Quizzes, and Notes inside Section

@admin.register(d_lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'content_type')
    list_filter = ('content_type', 'section__subject')
    search_fields = ('title', 'section__name')
    inlines = [SubsectionInline]  # Nested Subsections inside Lesson

@admin.register(e_subsection)
class SubsectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'lesson', 'video_url')
    list_filter = ('lesson__section__subject', 'lesson__content_type')
    search_fields = ('name', 'content', 'lesson__title')

@admin.register(f_quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('get_short_question', 'section')
    list_filter = ('section__subject',)
    search_fields = ('question', 'answer', 'section__name')

    def get_short_question(self, obj):
        return obj.question[:50] + '...' if len(obj.question) > 50 else obj.question
    get_short_question.short_description = 'Question'

@admin.register(g_note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'file_type')
    list_filter = ('file_type', 'section__subject')
    search_fields = ('title', 'section__name')