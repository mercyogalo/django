from django.shortcuts import render, redirect
from rings.models import student

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def student(request):
    return render(request, 'student.html')

def insertData(request):
    if request.method=="post":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        age=request.POST['age']
        image=request.FILES['image']
        
        students = Student(name=name, email=email, phone=phone, age=age, image=image)
        students.save()
        return redirect("./")
    
    
    return render(request, 'student.html')


def viewdata(request):
   students=Student.object.all()
return render(request, "viewdata.html", {'students': students})