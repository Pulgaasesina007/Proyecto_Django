from django.db import models

# Create your models here.
class project(models.Model):
 name = models.CharField( max_length=50 )
 Leader_project = models.CharField(max_length=60,default='En proceso de eleccion', blank=True)

 def __str__(self):
  return self.name

class task(models.Model):

 Tittle_task =  models.CharField(max_length= 200)
 Description_task = models.TextField()
 Project_Task = models.ForeignKey(project, on_delete=models.CASCADE)
 Done = models.BooleanField(default=False)
 def __str__(self):
  return  self.Tittle_task + '-' + self.Project_Task.name

