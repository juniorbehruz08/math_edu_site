from django.db import models
from django.contrib.auth.models import User
import random


def generate_unique_7_digit_code():
    while True:
        code = str(random.randint(1000000, 9999999))
        if not Profile.objects.filter(unique_code=code).exists():
            return code


def generate_class_code():
    while True:
        code = str(random.randint(1000000, 9999999))
        if not Classroom.objects.filter(class_code=code).exists():
            return code


class Profile(models.Model):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    unique_code = models.CharField(max_length=7, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = generate_unique_7_digit_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.role} - {self.unique_code}"


class Classroom(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_classes')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    class_code = models.CharField(max_length=7, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.class_code:
            self.class_code = generate_class_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.class_code}"


class JoinRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='join_requests')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='join_requests')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('classroom', 'student')

    def __str__(self):
        return f"{self.student.username} -> {self.classroom.name} ({self.status})"


class Homework(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='homeworks')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_homeworks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.classroom.name}"


class HomeworkAttachment(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='homework_files/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.homework.title} - {self.file.name}"


class StudentHomeworkFile(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='student_files')
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='student_homework_files')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_homework_files')
    file = models.FileField(upload_to='student_homework_files/')
    editor_content = models.TextField(blank=True, null=True)

    # ── NEW: submission tracking ──────────────────────────────────────
    submitted = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(null=True, blank=True)
    # ─────────────────────────────────────────────────────────────────

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('homework', 'student')

    def __str__(self):
        return f"{self.student.username} - {self.homework.title}"


class EditorImage(models.Model):
    """
    Stores images inserted via the browser editor.
    Each image is linked to the homework + student so they can be
    cleaned up if needed, and served back as a real URL.
    """
    homework  = models.ForeignKey(Homework,  on_delete=models.CASCADE, related_name='editor_images')
    student   = models.ForeignKey(User,      on_delete=models.CASCADE, related_name='editor_images')
    file      = models.ImageField(upload_to='editor_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} – {self.homework.title} – {self.file.name}"