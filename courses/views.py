from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Teacher, Course
from .forms import TeacherForm, CourseForm

# Home view
def home(request):
    return render(request, 'courses/home.html')

# Teacher Views
class TeacherListView(ListView):
    model = Teacher
    template_name = 'courses/teacher_list.html'
    context_object_name = 'teachers'
    paginate_by = 10

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'courses/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'courses/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'courses/teacher_form.html'
    success_url = reverse_lazy('teacher_list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'courses/teacher_confirm_delete.html'
    success_url = reverse_lazy('teacher_list')

# Course Views
class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 10

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

class CourseCreateView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')
