from django.db import models

# Create your models here.
class Tweet(models.Model):
    text = models.TextField()
    image = models.FileField(upload_to='images/', blank=True,null=True)