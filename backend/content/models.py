from django.db import models

class a_standard(models.Model):
    CLASS_CHOICES = [
        ('1st', '1st Standard'),
        ('2nd', '2nd Standard'),
        ('3rd', '3rd Standard'),
        ('4th', '4th Standard'),
        ('5th', '5th Standard'),
        ('6th', '6th Standard'),
        ('7th', '7th Standard'),
        ('8th', '8th Standard'),
        ('9th', '9th Standard'),
        ('10th', '10th Standard'),
    ]

    name = models.CharField(max_length=100, choices=CLASS_CHOICES)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Standard"
        verbose_name_plural = "Standards"


class b_subject(models.Model):
    standard = models.ForeignKey(a_standard, on_delete=models.CASCADE, related_name="subjects")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.standard.name})"

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"


class c_section(models.Model):
    subject = models.ForeignKey(b_subject, on_delete=models.CASCADE, related_name="sections")
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.subject.name})"

    class Meta:
        verbose_name = "Section"
        verbose_name_plural = "Sections"


class d_lesson(models.Model):
    section = models.ForeignKey(c_section, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    content_type = models.CharField(max_length=50, choices=[('video', 'Video'), ('text', 'Text')])

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"


class e_subsection(models.Model):
    lesson = models.ForeignKey(d_lesson, on_delete=models.CASCADE, related_name="subsections")
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.lesson.title})"

    class Meta:
        verbose_name = "Subsection"
        verbose_name_plural = "Subsections"


class f_quiz(models.Model):
    section = models.ForeignKey(c_section, on_delete=models.CASCADE, related_name="quizzes")
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"Quiz: {self.question[:50]}"

    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"


class g_note(models.Model):
    FILE_TYPE_CHOICES = [
        ('PDF', 'PDF'),
        ('DOC', 'Document'),
        ('TXT', 'Text'),
    ]

    title = models.CharField(max_length=200)
    section = models.ForeignKey(c_section, on_delete=models.CASCADE, related_name="notes")
    file_type = models.CharField(max_length=10, choices=FILE_TYPE_CHOICES, default='PDF')
    file = models.FileField(upload_to='notes/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Note"
        verbose_name_plural = "Notes"
