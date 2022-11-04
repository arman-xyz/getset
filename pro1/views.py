from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.


# This Function Will Add new Item and Show All Items
def addandshow(request):
 if request.method == 'POST':
  fm = StudentRegistration(request.POST)
  if fm.is_valid():
   nm = fm.cleaned_data['name']
   em = fm.cleaned_data['email']
   pw = fm.cleaned_data['password']
   reg = User(name=nm, email=em, password=pw)
   reg.save()
   messages.add_message(request,messages.SUCCESS,'Logged in successfully !!!')
   fm = StudentRegistration()
 else:
  fm = StudentRegistration()
 stud = User.objects.all()
 return render(request, 'pro1/addandshow.html', {'form':fm, 'stu':stud})



#This Function is for edit and update

def ed_update(request,id):
  if request.method == 'POST':
    pi = User.objects.get(pk=id)
    fm = StudentRegistration(request.POST,instance=pi)
    if fm.is_valid():
      fm.save()
  else:
    pi = User.objects.get(pk=id)
    fm = StudentRegistration(instance=pi)
  return render(request,'pro1/updatestudent.html',{'form':fm})




#This Function is for delete data

def delete_data(request,id):
  if request.method == 'POST':
    dl = User.objects.get(pk=id)
    dl.delete()
    # messages.add_message(request,messages.SUCCESS,'Deleted successfully !!!')
    return HttpResponseRedirect('/')
   













