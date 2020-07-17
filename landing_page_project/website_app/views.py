from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return render(request, "website_app/home2.html")

def test(request):
	return render(request, "website_app/test.html")

def product(request):
	return render(request, "website_app/product.html")

def pricing(request):
	return render(request, "website_app/pricing.html")

def search(request):
	return render(request, "website_app/search.html")	