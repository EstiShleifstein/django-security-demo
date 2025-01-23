from django.db import models

class User(models.Model):
  username = models.CharField(max_length=20)
  password = models.CharField(max_length=20)

class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  comment = models.CharField(max_length=100)
  creation_date = models.DateTimeField(auto_now_add=True)