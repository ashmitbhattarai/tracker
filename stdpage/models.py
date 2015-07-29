from django.db import models
from time import time
from django.utils import timezone
from django import forms

# Create your models here.
def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

# find the way to delete object ""	
		
class stdpage(models.Model):
	regno = models.IntegerField(max_length=8)
	fname = models.CharField(max_length=10)
	lname = models.CharField(max_length=10)
	sex = models.BooleanField()
	year = models.DateTimeField('year of admission')
	
class upoad1(models.Model):
	flname = models.CharField(max_length=30)
	thumbnail = models.FileField(upload_to=get_upload_file_name)
	def type(self):
		return self.thumbnail.split(".")

	def __unicode__(self):
		return self.id()

class status1(models.Model):
	stats = models.CharField(max_length = 250)
	syear = models.DateTimeField(auto_now_add = True, editable=False)
	user1 = models.CharField(max_length = 50)
	
	def __unicode__(self):
		return self.id()
		

class comment(models.Model):
	user_1 = models.CharField(max_length = 50)
	comments = models.CharField(max_length = 200)
	Status1 = models.ForeignKey(status1)
	pub_date = models.DateTimeField(auto_now_add = True, editable=False)
	
class asgmnt1(models.Model):
	subject = models.CharField(max_length=7)
	assignment = models.BooleanField(default = False)
	doi = models.DateTimeField('Date Of Submission(MM/DD/YYYY):')
	user = models.CharField(max_length = 20)
	submitted = models.BooleanField(default = False , editable = True)
	
	def timer(self):
		date = timezone.now()
		return self.doi - date
	def __unicode__(self):
		return self.id()
	


