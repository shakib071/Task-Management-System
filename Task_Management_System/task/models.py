from django.db import models

# Create your models here.

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField(max_length=100)
    is_Completed = models.BooleanField(default=False)
    taskAssignDate = models.DateField()


    def __str__(self):
        return self.taskTitle
    