from django import forms
from SampleApp.models import Student, Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['id', 'course_name']
