from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    path = models.ImageField(upload_to='media/')
    #creation_date = models.DateField(auto_now=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)