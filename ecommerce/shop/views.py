from django.shortcuts import render

# Create your views here.

def home(request):
    name="Joseph Ondieki"
    context={
        "name": name,
        "phone_number": 743264872,
        "gender":"female",  
         "experience":5,
    }
    return render(request, 'home.html', context)
def about(request):
    return render(request, 'about.html')
def shop(request):
    return render(request, 'shop.html')