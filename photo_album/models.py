from django.db import models
from django.contrib.auth.models import User



class Photo(models.Model):
    path = models.ImageField(upload_to='media/')
    creation_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    photo = models.ForeignKey(Photo, related_name="comments", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=64)
    comment = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
