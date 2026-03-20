from django.contrib import admin
from .models import (
    Profile,
    Classroom,
    JoinRequest,
    Homework,
    HomeworkAttachment,
    StudentHomeworkFile,
    EditorImage,
)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'unique_code')
    list_filter = ('role',)
    search_fields = ('user__username', 'unique_code')
    readonly_fields = ('unique_code',)


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'class_code', 'created_at')
    search_fields = ('name', 'teacher__username', 'class_code')
    readonly_fields = ('class_code', 'created_at')


@admin.register(JoinRequest)
class JoinRequestAdmin(admin.ModelAdmin):
    list_display = ('student', 'classroom', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('student__username', 'classroom__name')


class HomeworkAttachmentInline(admin.TabularInline):
    model = HomeworkAttachment
    extra = 1


class StudentHomeworkFileInline(admin.TabularInline):
    model = StudentHomeworkFile
    extra = 0
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'classroom', 'teacher', 'deadline', 'created_at')
    list_filter = ('classroom',)
    search_fields = ('title', 'classroom__name', 'teacher__username')
    inlines = [HomeworkAttachmentInline, StudentHomeworkFileInline]


@admin.register(HomeworkAttachment)
class HomeworkAttachmentAdmin(admin.ModelAdmin):
    list_display = ('homework', 'file', 'description')
    search_fields = ('homework__title',)


@admin.register(StudentHomeworkFile)
class StudentHomeworkFileAdmin(admin.ModelAdmin):
    list_display = ('student', 'homework', 'classroom', 'submitted', 'submitted_at', 'created_at', 'updated_at')
    list_filter = ('classroom', 'submitted')
    search_fields = ('student__username', 'homework__title')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(EditorImage)
class EditorImageAdmin(admin.ModelAdmin):
    list_display = ('student', 'homework', 'file', 'uploaded_at')
    list_filter = ('homework__classroom',)
    search_fields = ('student__username', 'homework__title')
    readonly_fields = ('uploaded_at',)