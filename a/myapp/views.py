from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import project, task
from .forms import create_new_task_form,create_new_project

from django.shortcuts import get_object_or_404
# Create your views here.

def index(request):

  tittle="Welcome to league of legends!!"

  return  render(request, 'templates/Index.html', {'tittle':tittle})
def hello(request,user):
  print(user)
  return HttpResponse("<h2>hola que hace: %s <h2/>" %user)

def about(request):
  lider = project.objects.get(id=5)
  return  render(request, 'templates/about.html', {'Username':lider})

def Project (request):
  projects= project.objects.all()
  return render(request, './project/templates/project/Project.html', {'projects':projects})
def tasks (request):
  tasks=task.objects.all()
  return render(request, './Task/templates/Task/Task.html', {'tasks':tasks})

def createtask(request):
  if request.method == 'GET':
    return render(request, 'Task/templates/Task/create_task.html', {'form':create_new_task_form()})
  else:
    task.objects.create(Tittle_task=request.POST['Tittle_task'],Description_task=request.POST['Description_task'],Project_Task_id=5)
    return redirect('/task/')
def create_porject(request):
  if request.method=='GET':
    return render(request, './project/templates/project/CreateProjects.html', {'form':create_new_project()})
  else:
    print(request.POST)
    project.objects.create(name=request.POST['name']),project.objects.create(Leader_project=request.POST['Leader_project'])
    return redirect(project)