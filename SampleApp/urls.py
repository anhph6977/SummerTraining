from django.urls import path
from SampleApp import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('hello/', views.hello_world),
    path('users/<int:id>', views.user),
    path('register/', views.registration),
    path('for-tag/', views.for_tag),
    path('if-tag/', views.if_tag),
    path('students/<int:pk>', views.StudentFormView.as_view()),
    path('students/', views.StudentListView.as_view()),
    path('courses/', views.CourseListView.as_view()),
    path('courses/create', views.CourseCreateView.as_view()),
    path('courses/<int:pk>', views.CourseDetailView.as_view()),
    path('courses/<int:pk>/update', views.CourseFormView.as_view()),
]
