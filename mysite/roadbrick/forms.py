from django import forms
from . models import Message, Post

class MessageForm(forms.ModelForm):

	Provider = forms.CharField(max_length=20, label = 'Truck Provider/Load Provider')
	class Meta:
		model = Message
		fields = ['Name', 'Email', 'Phone', 'Provider', 'Message',]
		
class PostForm(forms.ModelForm):

	Origin = forms.CharField(max_length = 20)
	Destination = forms.CharField(max_length = 20)
	Truck_Type = forms.CharField(max_length = 20, label = 'Truck Type' )
	Number_Of_Trucks = forms.CharField(max_length = 20, label = 'Number of Trucks' )
	Date_of_Journey = forms.CharField(max_length = 20, label = 'Date of Journey' )
	Time = forms.CharField(max_length = 20)
	Weight = forms.CharField(max_length = 20, label = 'Weight(in Ton)')
	Material_Name = forms.CharField(max_length = 20, label = 'Material Name' )
	class Meta:
		model = Post
		fields = ["Origin", "Truck_Type", "Date_of_Journey", "Weight", "Material_Name", "Destination", "Number_Of_Trucks", "Time", "Name", "Phone", ]