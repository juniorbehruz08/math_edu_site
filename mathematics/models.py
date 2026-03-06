from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


class Lessons(models.Model):
    lesson_name = models.CharField(max_length=50, verbose_name='Language')
    url = models.CharField(max_length=200, verbose_name='URL')

    def __str__(self):
        return self.lesson_name

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class TakenLessons(models.Model):
    lesson = models.CharField(max_length=50, verbose_name='Lesson')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='taken_lessons')
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson

    class Meta:
        verbose_name = 'Taken Lesson'
        verbose_name_plural = 'Taken Lessons'


from django.contrib.auth.models import User


class MathTestResult(models.Model):

    """
    Stores one completed math test session per record.
    Fields match the JSON payload sent from math-test.html.
    """

    # Link to user (optional — remove if you don't use auth)
    lesson = models.ForeignKey(Lessons, on_delete=models.CASCADE, related_name='math_test_results')


    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='math_test_results',
    )

    # ── Core scores ──────────────────────────────────────────────
    correct = models.PositiveIntegerField()
    wrong = models.PositiveIntegerField()
    total_questions = models.PositiveIntegerField(default=30)
    correct_percentage = models.PositiveSmallIntegerField(
        help_text="0–100"
    )

    # ── Timing ───────────────────────────────────────────────────
    time_spent_seconds = models.PositiveIntegerField(
        help_text="Total seconds spent on the test"
    )
    time_spent_display = models.CharField(
        max_length=20,
        help_text="Human-readable e.g. '12m 34s'"
    )
    avg_time_per_question_seconds = models.FloatField(
        help_text="Average seconds per question"
    )

    # ── Meta ─────────────────────────────────────────────────────
    test_taken_at = models.CharField(
        max_length=60,
        help_text="Locale string from the browser e.g. '2/21/2026, 3:45:00 PM'"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    questions_json_formatted = models.JSONField(verbose_name="Questions JSON", null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Math Test Result'
        verbose_name_plural = 'Math Test Results'

    def __str__(self):
        user_label = self.user.username if self.user else 'Anonymous'
        return (
            f"{user_label} | {self.correct}/{self.total_questions} "
            f"({self.correct_percentage}%) | {self.test_taken_at}"
        )

from django.utils import timezone
import datetime

class PendingUser(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    country = models.CharField(max_length=150, null=True)
    email = models.EmailField()
    password = models.CharField(max_length=255)  # hashed
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_expired(self):
        return timezone.now() > self.created_at + datetime.timedelta(minutes=5)

    def __str__(self):
        return self.email


class Country(models.Model):
    country = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='country')
    def __str__(self):
        return self.country


class Feedback(models.Model):
    TYPE_CHOICES = [
        ('recommendation', 'Recommendation'),
        ('problem', 'Problem Report'),
    ]

    sender_name = models.CharField(max_length=100, default='Anonymous')
    message_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='recommendation')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_message_type_display()}] {self.sender_name} — {self.created_at:%Y-%m-%d %H:%M}"