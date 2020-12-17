from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class TodoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    work = models.CharField(max_length=200, null=False)
    creation_Time = models.DateTimeField(auto_now_add=True)
    completion_Status = models.BooleanField(default=False)

    def __str__(self):
        return self.work
