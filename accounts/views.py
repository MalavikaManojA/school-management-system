from django.shortcuts import render,redirect,HttpResponse
from .models import Contact,User
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
# Create your views here.

def signin(request):
    if request.method=='GET':
        return render(request,'accounts/login.html')
    elif request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        user=authenticate(request, username=uname, password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('admin_page')
            elif user.is_staff:
                return redirect('staff_home')
            else:
                return redirect('home')
            
        else:
            
            messages.add_message(request, messages.ERROR, 'Invalid Username / Password')
            return redirect("signin")
            # return HttpResponse("Failed")
        
def action_logout(request):
    logout(request)
    return redirect('signin')
        
def home(request):
    return render(request, 'accounts/shared/base.html')

def about_page(request):
    return render(request,'accounts/about.html')

def contact_page(request):
    if request.method=='GET':
        return render(request,'accounts/contact.html')
    elif request.method=='POST':
        c_name=request.POST['c_name']
        from_email=request.POST['from_mail']
        subject=request.POST['subject']
        body=request.POST['body']
        obj=Contact.objects.create(c_name=c_name, from_mail=from_email, subject=subject, body=body)
        obj.save()
        return redirect('contact')
    

def change_password(request):
    if request.method=='GET':
        return render(request,'accounts/change_password.html', {'form': PasswordChangeForm(user=request.user)})
    elif request.method=='POST':
        form = PasswordChangeForm(request.user, instance=request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'accounts/change_password.html', {'form': form})
        return redirect('home')
                
        
