from django.db import models

class Show(models.Model):
  name = models.CharField(max_length=45)
  network = models.CharField(max_length=45)
  release_date = models.DateTimeField(max_length=45)
  Description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
