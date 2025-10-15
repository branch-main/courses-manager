from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # Teacher URLs
    path('teachers/', views.TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/create/', views.TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/update/', views.TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete/', views.TeacherDeleteView.as_view(), name='teacher_delete'),
    
    # Course URLs
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('courses/create/', views.CourseCreateView.as_view(), name='course_create'),
    path('courses/<int:pk>/update/', views.CourseUpdateView.as_view(), name='course_update'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),
]
