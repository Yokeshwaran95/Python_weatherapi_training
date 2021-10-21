from django.db import models

# Create your models here.


class Employee(models.Model):
	Name=models.CharField(max_length=100)
	Age=models.IntegerField(default=1)
	City=models.CharField(max_length=100)
	Designation=models.CharField(max_length=500)

	def __str__(self):
		return self.Name