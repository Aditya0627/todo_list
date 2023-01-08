from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank=True) #cascade is used so that if a user has deleted itself all the data related to the user will be deleted
    title = models.CharField(max_length=200, null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):

        return self.title

    class Meta:
        ordering = ['complete']