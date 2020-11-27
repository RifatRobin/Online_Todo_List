from django.db import models

# Create your models here.


class TodoList(models.Model):
    work = models.CharField(max_length=200)
    creation_Time = models.DateTimeField(auto_now_add=True)
    completion_Status = models.BooleanField(default=False)

    def __str__(self):
        return self.work
