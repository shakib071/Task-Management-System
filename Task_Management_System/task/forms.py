from django import forms 
from .models import TaskModel

class taskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
