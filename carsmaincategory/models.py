from django.db import models

class Cars(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField(max_length=4)
    content = models.TextField(blank=True)
    data_create = models.DateTimeField(auto_now_add=True)
    data_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)