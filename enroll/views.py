from django.shortcuts import render, HttpResponse
from .forms import StudentRegistration
from .models import User

# Create your views here.

#..Adding new student....
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
             nm = fm.cleaned_data['name']
             em = fm.cleaned_data['email']
             pw = fm.cleaned_data['password']
             reg = User(name=nm, email=em, password=pw)
             reg.save()
             fm = StudentRegistration() 
             
    else:
          fm = StudentRegistration() 
          
    stud = User.objects.all()
    
    return render(request, r'C:\Users\Nirmal\Desktop\django_crud_project\crudproject\enroll\templates\enroll\adandshow.html', {'form': fm, 'stu':stud})


#..updating student....
def update_data(request, id):
     if request.method == 'POST':
          pi = User.objects.get(pk=id)
          fm = StudentRegistration(request.POST, instance=pi)
          if fm.is_valid():
               fm.save()
          else:
               pi = User.objects.get(pk=id) 
               fm = StudentRegistration(instance=id)   
     return render(request, r'C:\Users\Nirmal\Desktop\django_crud_project\crudproject\enroll\templates\enroll\updatestudent.html', {'form': fm})

#..Delete existing student....
def delete_data(request, id):
     if request.method =='POST':
          pi = User.objects.get(pk=id)
          pi.delete()
          return HttpResponse('/')
