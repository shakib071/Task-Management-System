from django.shortcuts import render,redirect
from .forms import taskCategoryForm

# Create your views here.

def add_category(request):
    if request.method == "POST":
        add_category_form = taskCategoryForm(request.POST)
        if add_category_form.is_valid():
            add_category_form.save()
            return redirect('homepage')
    else:
        add_category_form = taskCategoryForm()
    return render(request,'add_category.html',{'form':add_category_form})
