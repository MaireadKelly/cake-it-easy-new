from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home/home.html')

def shop(request):
    return render(request, 'home/shop.html')  # Assuming you have a `shop.html` template
