from django.db import transaction
from SampleApp.models import Student, Course


def run():
    student_data = {
        'first_name': 'John',
        'last_name': 'Doe',
        'login': 'john',
        'password': 'admin321'
    }
    student = Student(**student_data)
    course_data = {
        'course_name': 'my course'
    }
    course = Course(**course_data)
    try:
        with transaction.atomic():
            student.save()
            course.save()
            course.students.add(student)
            raise Exception() # raise an exception to simulate error
    except:
        pass
    print(student, course)