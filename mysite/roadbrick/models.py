from django.db import models

class Message(models.Model):

	Name = models.CharField(max_length=30)
	Email = models.CharField(max_length=30)
	Phone = models.CharField(max_length=20)
	Provider = models.CharField(max_length=20)
	Message = models.TextField(max_length='200')
	
class Post(models.Model):

	Origin = models.CharField(max_length=20)
	Destination = models.CharField(max_length=20)	
	Truck_Type = models.CharField(max_length=20)
	Number_Of_Trucks = models.CharField(max_length=20)
	Date_of_Journey = models.CharField(max_length=20)
	Time = models.CharField(max_length=30)
	Weight = models.CharField(max_length=20)
	Material_Name = models.CharField(max_length=20)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	Name = models.CharField(max_length=20)
	Phone = models.CharField(max_length=20)
	
	
