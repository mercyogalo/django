from django.shortcuts import render

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
    return render(request,'contact.html')

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

def  starterPage(request):
    return render(request, 'starter-page.html')

def team(request):
    return render(request, 'team.html')

def testimonials(request):
    return render(request,'testimonials.html')