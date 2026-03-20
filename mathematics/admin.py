# admin.py

from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Count
from .models import Lessons, TakenLessons, MathTestResult, PendingUser, Country, Feedback


# ───────────────────────────────────────────
# Lessons
# ───────────────────────────────────────────
@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson_name', 'url')
    search_fields = ('lesson_name',)
    ordering = ('lesson_name',)


# ───────────────────────────────────────────
# TakenLessons
# ───────────────────────────────────────────
@admin.register(TakenLessons)
class TakenLessonsAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson', 'user', 'date_taken')
    search_fields = ('lesson', 'user__username')
    list_filter = ('date_taken','lesson')
    ordering = ('-date_taken',)


# ───────────────────────────────────────────
# MathTestResult
# ───────────────────────────────────────────
@admin.register(MathTestResult)
class MathTestResultAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'user', 'lesson', 'correct', 'wrong',
        'total_questions', 'correct_percentage',
        'time_spent_display', 'test_taken_at', 'created_at'
    )
    search_fields = ('user__username', 'lesson__lesson_name')
    list_filter = ('lesson', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)


# ───────────────────────────────────────────
# PendingUser
# ───────────────────────────────────────────
@admin.register(PendingUser)
class PendingUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'country', 'code', 'created_at', 'is_expired')
    search_fields = ('username', 'email', 'country')
    list_filter = ('country', 'created_at')
    ordering = ('-created_at',)

    def is_expired(self, obj):
        return obj.is_expired()

    is_expired.boolean = True
    is_expired.short_description = 'Expired?'


# ───────────────────────────────────────────
# Country
# ───────────────────────────────────────────
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'country')
    search_fields = ('user__username', 'country')
    list_filter = ('country',)


# ───────────────────────────────────────────
# Monitoring (proxy model orqali)
# ───────────────────────────────────────────
class UserMonitoringProxy(User):
    class Meta:
        proxy = True
        verbose_name = 'User Monitoring'
        verbose_name_plural = '📊 User Monitoring'


@admin.register(UserMonitoringProxy)
class UserMonitoringAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'username', 'email', 'first_name', 'last_name',
        'get_country', 'date_joined', 'is_active'
    )
    search_fields = ('username', 'email', 'country__country')
    list_filter = ('country__country', 'is_active', 'date_joined')
    ordering = ('-date_joined',)
    readonly_fields = ('date_joined', 'last_login')

    def get_country(self, obj):
        try:
            return obj.country.country
        except Exception:
            return '—'

    get_country.short_description = 'Country'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}

        total_users = User.objects.count()
        active_users = User.objects.filter(is_active=True).count()
        by_country = (
            Country.objects
            .values('country')
            .annotate(total=Count('id'))
            .order_by('-total')
        )

        extra_context['total_users'] = total_users
        extra_context['active_users'] = active_users
        extra_context['by_country'] = by_country

        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('sender_name', 'message_type', 'message', 'is_read', 'created_at')
    list_display_links = ('sender_name',)
