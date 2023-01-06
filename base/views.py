from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Task
from django.urls import reverse_lazy

# Create your views here.

class TaskList(ListView):
    #will look for html with name model_list.html
    model = Task
    context_object_name = "tasks"

class TaskDetail(DetailView):
    #will look for html with name model_detail.html
    model = Task
    context_object_name = "tasks_detail"
    # template_name = 'base/task.html' we can change the name of the html file

class TaskCreate(CreateView):
    #will look for html with name model_form.html
    model = Task
    fields = '__all__' 
    success_url = reverse_lazy('tasks')  #this is used to redirect after submitting the form
