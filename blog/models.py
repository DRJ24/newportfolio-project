from django.db import models
from datetime import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now(), blank=True)
    body = models.TextField(max_length=200)
    image = models.ImageField(upload_to='images/')
