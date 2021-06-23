from django.db import models

# Create your models here.
class Category(models.Model):
	gemType = models.CharField(max_length=100, null=False, blank=False)
	
	def __str__(self):
		return self.gemType


class Photo(models.Model):
	gemName = models.CharField(max_length=100, null=False, blank=True)
	activePassive = models.CharField(max_length=100, null=False, blank=True)
	category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
	image = models.ImageField(null=False,blank=False)
	description = models.TextField()

	def __str__(self):
		return self.gemName

