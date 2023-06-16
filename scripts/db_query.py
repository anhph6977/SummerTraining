from SampleApp.models import Student, Course
from django.db.models import Count, F, Avg, Max

def run():
    queryset = Course.objects.annotate(num_students=Count("students", distinct=True)).filter(num_students__gt=2)
    print(queryset)
    queryset = Course.objects.annotate(avg_students=Avg("students"),
                                       num_students=Count("students", distinct=True)).filter(
        num_students__gt=F('avg_students'))
    print(queryset)

    queryset = Course.objects.filter(course_name=F('students__first_name'))
    print(queryset)