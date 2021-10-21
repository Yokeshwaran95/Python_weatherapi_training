from django.shortcuts import render
from django.http import HttpResponse
from welcome.models import Employee
import requests

# Create your views here.

def home(request):
	data=Employee.objects.filter(City__icontains="ch")
	return render(request,"home.html",{"context":data})

def contact(request):
	# print(request.POST)
	if request.method=="POST":
		cityname=request.POST.get("city")
		countryname=request.POST.get("country")

		print(cityname)
		print(countryname)
	# 	print(request.POST.get("city"))
		url="http://api.openweathermap.org/data/2.5/weather?q="+cityname+"&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1"
		response=requests.get(url)
		response_out=response.json()
		print(response_out)

	return render(request,"contact.html")



