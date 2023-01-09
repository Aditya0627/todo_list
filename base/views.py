from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#there is slight change in the code file
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks'
)


class TaskList(LoginRequiredMixin,ListView):
    #will look for html with name model_list.html
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            # context["color"] = 'red'
            # print(self.request.user)
            context['tasks'] = context['tasks'].filter(user = self.request.user)
            context['count'] = context['tasks'].filter(complete =False).count()

            return context
        

class TaskDetail(LoginRequiredMixin,DetailView):
    #will look for html with name model_detail.html
    model = Task
    context_object_name = "tasks_detail"
    # template_name = 'base/task.html' we can change the name of the html file

class TaskCreate(LoginRequiredMixin,CreateView):
    #will look for html with name model_form.html
    model = Task
    fields = {'title','complete','description'} 
    success_url = reverse_lazy('tasks')  #this is used to redirect after submitting the form
    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_invalid(form)
        
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = {'title','complete','description'} 
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task   #look for html file with model_confirm_delete.html
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

