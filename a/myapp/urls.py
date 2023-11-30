from django.urls import  path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('task/', views.tasks, name='task'),
    path('project_1/', views.Project, name='project'),
    path('hello/<str:user>', views.hello, name='hello'),
    path('CreateTask/', views.createtask, name='CreateTask'),
    path('CreateProject/', views.create_porject, name='CreateProject')
]