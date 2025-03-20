from django import forms

from .models import taskCategoryModel 

class taskCategoryForm(forms.ModelForm):
    class Meta:
        model = taskCategoryModel
        fields = '__all__'