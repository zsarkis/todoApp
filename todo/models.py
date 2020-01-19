from django.db import models

# Create your models here.

class TodoItem(models.Model):
    content = models.TextField()
    user_id = models.IntegerField()
