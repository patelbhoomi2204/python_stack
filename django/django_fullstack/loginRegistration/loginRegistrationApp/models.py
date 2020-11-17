from django.db import models
import re
import bcrypt

class UserManager(models.Manager):
  def regValidator(self, postData):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    userswithSameemail = User.objects.filter(email = postData['email'])
    print(userswithSameemail)
    errors = {}
    if len(postData['fname']) == 0:
      errors["fnameReq"] = "First Name is reuqired!"
    elif len(postData['fname']) < 2:
      errors["fnameLen"] = "First Name must be 2 characters long!"
    if len(postData['lname']) == 0:
      errors["lnameReq"] = "Last Name is required!"
    elif len(postData['lname']) < 2:
      errors["lnameLen"] = "Last Name must be 2 characters long!"
    if len(postData['email']) == 0:
      errors["emailReq"] = "Email is reuqired!"
    elif not EMAIL_REGEX.match(postData['email']):
      errors['emailPattern'] = "Email is not valid!"
    elif len(userswithSameemail)>0:
      errors['emailregistered'] = "Email is already registered!"
    if len(postData['pw']) < 8:
      errors['PWlen'] = "Password must be 8 characters long!"
    if postData['pw'] != postData['pwc']:
      errors["pwMatch"] = "Password and confirm PW should match!"
    return errors

  def loginValidator(self, postData):
    errors = {}
    userswithSameemail = User.objects.filter(email = postData['email'])
    if len(userswithSameemail) == 0:
      errors['emailNotFound'] = "This email is not registered yet. Please register first"
    if not bcrypt.checkpw(postData['pw'].encode(), userswithSameemail[0].password.encode()):
      errors['incorrectPW'] = "Password is incorrect!"
    return errors

class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  confirm_PW = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  objects = UserManager()
