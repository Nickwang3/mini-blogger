from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MiniBlog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now=True)

class MiniBlogReply(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now=True)
    replied_to = models.ForeignKey(MiniBlog, on_delete=models.DO_NOTHING)    

class MiniBlogRepost(models.Model):
    pass

class MiniBlogQuote(models.Model):
    pass