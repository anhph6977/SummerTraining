from RestFramework.serializers import CourseSerializer
from SampleApp.models import Student, Course


def run():
    courses = Course.objects.all().prefetch_related('students')
    course_serializer = CourseSerializer(courses, many=True)
    print(course_serializer.data)
