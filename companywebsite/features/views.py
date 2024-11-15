from django.shortcuts import render,redirect
from .models import Messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request,'about.html')

def blogDetails(request):
    return render(request, 'blog-details.html')

def blog(request):
    return render(request,'blog.html')





def contact(request):
    context = {}
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject'].lower()  # Fixing the .lower() usage
        message = request.POST['message']
        
        
        eachMessage=Messages(name=name, email=email, subject=subject, message=message)
        eachMessage.save()
        redirect('./')
        context['submit_message']=f"Thank you {name} for contacting us. Your issue on {subject} will be addressed with our team shortly."
    
    return render(request, 'contact.html', context)

  



def portfolioDetails(request):
    return render(request, 'portfolio-details.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def pricing(request):
    return render(request, 'pricing.html')

def serviceDetails(request):
    return render(request, 'service-details.html')

def services(request):
    return render(request, 'services.html')


def team(request):
    return render(request, 'team.html')

def testimonials(request):
    return render(request,'testimonials.html')