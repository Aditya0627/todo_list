from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks'
)


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

class TaskUpdate(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class TaskDelete(DeleteView):
    model = Task   #look for html file with model_confirm_delete.html
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

