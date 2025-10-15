from django.contrib import admin
from .models import Teacher, Course

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'speciality']
    search_fields = ['name', 'speciality']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'teacher', 'description']
    list_filter = ['teacher']
    search_fields = ['name', 'description']
