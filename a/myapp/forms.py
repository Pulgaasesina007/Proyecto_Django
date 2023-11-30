from django import forms

class create_new_task_form(forms.Form):
    Tittle_task = forms.CharField(label="Titulo de tarea",max_length=200)
    Description_task = forms.CharField( widget= forms.Textarea,label="Descripcion de la tarea ")

class create_new_project(forms.Form):
    name = forms.CharField(label='Nombre del proyecto',max_length=200)
    Leader_project= forms.CharField(label='Lider del proyecto',max_length=30)