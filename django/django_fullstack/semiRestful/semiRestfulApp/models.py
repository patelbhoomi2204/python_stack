from django.db import models
from datetime import date

class ShowManager(models.Manager):
    def createShowValidator(self, postData):
        errors = {}
        today = date.today()
        if len(postData['title']) == 0:
          errors['titleReq'] = "Title is required!"
        elif len(postData['title']) <= 3:
          errors['titlelength'] = "Title must be longer than 3 character!"
        if len(postData['desc']) == 0:
          errors['descReq'] = "Description required!"
        elif len(postData['desc']) <= 10:
          errors['desclength'] = "Description must be longer than 10 characters!"
        if len(postData['rel']) == 0:
          errors['relReq'] = "Release date required."
        elif postData['rel'] > str(today) :
          errors['rel'] = "Can not add show which is not released yet!"
        if len(postData['network']) == 0:
          errors['netReq'] = "Network is required!"
        return errors

class Show(models.Model):
  name = models.CharField(max_length=45)
  network = models.CharField(max_length=45)
  release_date = models.DateTimeField(max_length=45)
  Description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  objects = ShowManager()