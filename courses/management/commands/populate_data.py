from django.core.management.base import BaseCommand
from courses.models import Teacher, Course


class Command(BaseCommand):
    help = 'Poblar la base de datos con profesores y cursos de ejemplo'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creando datos de ejemplo...')

        # Eliminar datos existentes
        Course.objects.all().delete()
        Teacher.objects.all().delete()
        self.stdout.write('Datos anteriores eliminados')

        # Crear profesores
        teachers_data = [
            {'name': 'Dr. Juan Pérez', 'speciality': 'Ciencias de la Computación'},
            {'name': 'Prof. María García', 'speciality': 'Matemáticas'},
            {'name': 'Dr. David Chen', 'speciality': 'Física'},
            {'name': 'Prof. Ana Martínez', 'speciality': 'Desarrollo Web'},
            {'name': 'Dr. Carlos Rodríguez', 'speciality': 'Ciencia de Datos'},
        ]

        teachers = []
        for teacher_data in teachers_data:
            teacher = Teacher.objects.create(**teacher_data)
            teachers.append(teacher)
            self.stdout.write(self.style.SUCCESS(f'Profesor creado: {teacher.name}'))

        # Crear cursos
        courses_data = [
            {
                'name': 'Introducción a la Programación en Python',
                'description': 'Aprende los fundamentos de la programación en Python incluyendo variables, tipos de datos, estructuras de control, funciones y programación orientada a objetos. ¡Perfecto para principiantes!',
                'teacher': teachers[0]
            },
            {
                'name': 'Desarrollo Web Avanzado con Django',
                'description': 'Domina el framework Django construyendo aplicaciones web del mundo real. Los temas incluyen modelos, vistas, plantillas, formularios, autenticación y despliegue.',
                'teacher': teachers[3]
            },
            {
                'name': 'Cálculo y Álgebra Lineal',
                'description': 'Curso completo que cubre cálculo diferencial e integral, junto con operaciones de matrices, espacios vectoriales y transformaciones lineales.',
                'teacher': teachers[1]
            },
            {
                'name': 'Ciencia de Datos con Python',
                'description': 'Explora análisis de datos, visualización y aprendizaje automático usando librerías de Python como pandas, matplotlib y scikit-learn.',
                'teacher': teachers[4]
            },
            {
                'name': 'Fundamentos de Física Cuántica',
                'description': 'Introducción a la mecánica cuántica, dualidad onda-partícula, ecuación de Schrödinger y entrelazamiento cuántico.',
                'teacher': teachers[2]
            },
            {
                'name': 'Algoritmos de Aprendizaje Automático',
                'description': 'Profundiza en algoritmos de aprendizaje supervisado y no supervisado, redes neuronales y aplicaciones prácticas de IA.',
                'teacher': teachers[4]
            },
            {
                'name': 'Diseño Web con HTML, CSS y JavaScript',
                'description': 'Crea sitios web hermosos y responsivos usando tecnologías web modernas. Incluye proyectos prácticos y mejores prácticas.',
                'teacher': teachers[3]
            },
            {
                'name': 'Matemáticas Discretas',
                'description': 'Estudia lógica, teoría de conjuntos, teoría de grafos, combinatoria y sus aplicaciones en ciencias de la computación.',
                'teacher': teachers[1]
            },
            {
                'name': 'Bases de Datos Relacionales',
                'description': 'Aprende diseño de bases de datos, SQL, normalización y optimización de consultas. Incluye proyectos con PostgreSQL y MySQL.',
                'teacher': teachers[0]
            },
            {
                'name': 'Inteligencia Artificial Aplicada',
                'description': 'Descubre aplicaciones prácticas de IA en visión por computadora, procesamiento de lenguaje natural y sistemas de recomendación.',
                'teacher': teachers[4]
            },
        ]

        for course_data in courses_data:
            course = Course.objects.create(
                name=course_data['name'],
                description=course_data['description'],
                teacher=course_data['teacher']
            )
            self.stdout.write(self.style.SUCCESS(f'Curso creado: {course.name}'))

        self.stdout.write(self.style.SUCCESS('¡Datos de ejemplo creados exitosamente!'))
        self.stdout.write(f'Total de profesores: {Teacher.objects.count()}')
        self.stdout.write(f'Total de cursos: {Course.objects.count()}')
