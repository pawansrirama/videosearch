from django.db import models


class registerDetials(models.Model):

	firstName = models.CharField(max_length=50,blank=False)
	lastName = models.CharField(max_length=50,blank=False)
	birthdayDate = models. DateTimeField (null=False)
	gender = models.CharField(max_length=100,null=False)
	emailAddress = models.CharField(max_length=100,blank=False)
	phoneNumber = models.CharField(max_length=13,blank=False)
	password = models.CharField(max_length=50,null=False)

	def __str__(self):
		return self.firstName

