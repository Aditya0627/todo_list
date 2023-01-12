from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.detail import DetailView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
#there is slight change in the code file
class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
        
class RegisterPage(FormView):

    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')  #this is used to redirect after submitting the form
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

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
            search_input = self.request.GET.get('search-area') or ''
            if search_input:
                context['tasks'] = context['tasks'].filter(title__startswith=search_input)
            context['search_input'] = search_input
            return context
        

class TaskDetail(LoginRequiredMixin,DetailView):
    #will look for html with name model_detail.html
    model = Task
    context_object_name = "tasks_detail"
    # template_name = 'base/task.html' we can change the name of the html file

class TaskCreate(LoginRequiredMixin,CreateView):
    #will look for html with name model_form.html
    model = Task
    # fields = '__all__'

    fields = {'title','complete','description'} 
    # fields = {'complete','description','title'} 
    # print(self.request.user)
    success_url = reverse_lazy('tasks')  #this is used to redirect after submitting the form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)

        
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = {'complete','description','title'} 
    success_url = reverse_lazy('tasks')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task   #look for html file with model_confirm_delete.html
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')



