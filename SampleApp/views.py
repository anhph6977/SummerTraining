from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView

from SampleApp.forms import StudentForm, CourseForm
from SampleApp.models import Student, Course


# Create your views here.
def hello_world(request):
    return HttpResponse('<h1>Hello World</h1>')


def welcome(request):
    return render(request, 'Welcome.html', {"first_name": "My First Name"})


def user(request, id):
    message = f"<h1>You have request access to user with id: {str(id)}</h1>"
    return HttpResponse(message)


def registration(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registration success!")
        else:
            print(form.errors)
    return render(request, "Registration.html")


def for_tag(request):
    my_list = [
        {'id': 1, 'name': 'First User'},
        {'id': 2, 'name': 'Second User'}
    ]
    return render(request, 'ForTag.html', {'my_list': my_list})


def if_tag(request):
    return render(request, "IfTag.html", {'condition': True})


from django.views.generic.edit import UpdateView, CreateView


class StudentFormView(UpdateView):
    template_name = "Student.html"
    form_class = StudentForm
    success_url = "/sample-app/students/"
    queryset = Student.objects.all()


from django.views.generic.list import ListView


class StudentListView(ListView):
    template_name = "StudentList.html"
    queryset = Student.objects.all()


class CourseCreateView(CreateView):
    template_name = "CourseCreate.html"
    form_class = CourseForm
    success_url = "/sample-app/courses/"


class CourseFormView(UpdateView):
    template_name = "Course.html"
    form_class = CourseForm
    success_url = "/sample-app/courses/"
    queryset = Course.objects.all()


class CourseDetailView(DetailView):
    template_name = "CourseDetail.html"
    queryset = Course.objects.all()


class CourseListView(ListView):
    template_name = "CourseList.html"
    queryset = Course.objects.all()
from django.db.models import Count
Course.objects.annotate(num_students=Count("students", distinct=True)).filter(num_students__gt=2)