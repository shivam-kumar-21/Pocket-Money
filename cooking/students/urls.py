from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('student_details/', views.student_details_list, name="student_details_list"),
    path('student_entry/', views.student_entry, name="student-entry")
]