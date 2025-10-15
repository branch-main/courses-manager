from django.db import models
from django.urls import reverse

class Teacher(models.Model):
    name = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('teacher_detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['name']

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['name']
