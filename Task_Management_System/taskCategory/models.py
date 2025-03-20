from django.db import models
from task.models import TaskModel

# Create your models here.

class taskCategoryModel(models.Model):
    categoryName = models.CharField(max_length=100)
    tasks = models.ManyToManyField(TaskModel, related_name='categories')


    def __str__(self):
        return self.categoryName
