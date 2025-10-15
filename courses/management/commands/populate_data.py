from django.core.management.base import BaseCommand
from courses.models import Teacher, Course


class Command(BaseCommand):
    help = 'Populate database with sample teachers and courses'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')

        # Create teachers
        teachers_data = [
            {'name': 'Dr. John Smith', 'speciality': 'Computer Science'},
            {'name': 'Prof. Maria Garcia', 'speciality': 'Mathematics'},
            {'name': 'Dr. David Chen', 'speciality': 'Physics'},
            {'name': 'Prof. Sarah Johnson', 'speciality': 'Web Development'},
            {'name': 'Dr. Michael Brown', 'speciality': 'Data Science'},
        ]

        teachers = []
        for teacher_data in teachers_data:
            teacher, created = Teacher.objects.get_or_create(**teacher_data)
            teachers.append(teacher)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created teacher: {teacher.name}'))

        # Create courses
        courses_data = [
            {
                'name': 'Introduction to Python Programming',
                'description': 'Learn the fundamentals of Python programming including variables, data types, control structures, functions, and object-oriented programming. Perfect for beginners!',
                'teacher': teachers[0]
            },
            {
                'name': 'Advanced Django Web Development',
                'description': 'Master Django framework by building real-world web applications. Topics include models, views, templates, forms, authentication, and deployment.',
                'teacher': teachers[3]
            },
            {
                'name': 'Calculus and Linear Algebra',
                'description': 'Comprehensive course covering differential and integral calculus, along with matrix operations, vector spaces, and linear transformations.',
                'teacher': teachers[1]
            },
            {
                'name': 'Data Science with Python',
                'description': 'Explore data analysis, visualization, and machine learning using Python libraries like pandas, matplotlib, and scikit-learn.',
                'teacher': teachers[4]
            },
            {
                'name': 'Quantum Physics Fundamentals',
                'description': 'Introduction to quantum mechanics, wave-particle duality, the Schrödinger equation, and quantum entanglement.',
                'teacher': teachers[2]
            },
            {
                'name': 'Machine Learning Algorithms',
                'description': 'Deep dive into supervised and unsupervised learning algorithms, neural networks, and practical applications of AI.',
                'teacher': teachers[4]
            },
            {
                'name': 'Web Design with HTML, CSS, and JavaScript',
                'description': 'Create beautiful and responsive websites using modern web technologies. Includes hands-on projects and best practices.',
                'teacher': teachers[3]
            },
            {
                'name': 'Discrete Mathematics',
                'description': 'Study logic, set theory, graph theory, combinatorics, and their applications in computer science.',
                'teacher': teachers[1]
            },
        ]

        for course_data in courses_data:
            course, created = Course.objects.get_or_create(
                name=course_data['name'],
                defaults={
                    'description': course_data['description'],
                    'teacher': course_data['teacher']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created course: {course.name}'))

        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
        self.stdout.write(f'Total teachers: {Teacher.objects.count()}')
        self.stdout.write(f'Total courses: {Course.objects.count()}')
