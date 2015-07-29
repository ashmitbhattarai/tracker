from django.db import models
from time import time
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
# Create your models here.

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)	


class newuser(models.Model):
	
	regdnum  = models.CharField(max_length=8)
	user = models.OneToOneField(User)
	propic = models.FileField(upload_to = get_upload_file_name)
	semester = models.CharField(max_length = 1)
	depart = models.CharField(max_length = 10)	
	
User.profile =property(lambda u : newuser.objects.get_or_create(user = u)[0])

