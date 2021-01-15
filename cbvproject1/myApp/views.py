from django.shortcuts import render
from myApp.models import Student
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
class StudentListView(ListView):
    model=Student
class StudentDetailView(DetailView):
    model=Student
class StudentCreateView(CreateView):
    model=Student
    fields=('name','number','marks','place')
class StudentUpdateView(UpdateView):
    model=Student
    fields=('name','marks')
class StudentDeleteView(DeleteView):
    model=Student
    success_url=reverse_lazy('students')
