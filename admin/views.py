from django.shortcuts import render,redirect
from .forms import UserForm, StaffDetailForm, StaffDetail,UserEditForm,SubjectForm
from django.core.mail import send_mail
from staff.forms import *
# Create your views here.
def admin_page(request):
    context={}
    context['data']=StaffDetail.objects.all()
    return render(request,'admin/admin_page.html',context=context)

def staff_signup(request):
    if request.method=='GET':
        context={
            'form1': UserForm(),
            'form2': StaffDetailForm()
        }
        return render(request,'admin/staff_signup.html', context=context)
    elif request.method=='POST':
        form1=UserForm(request.POST,request.FILES)
        form2=StaffDetailForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            obj1=form1.save(commit=False)
            obj2=form2.save(commit=False)
            obj1.set_password(form1.cleaned_data['password'])
            obj2.staff_name=obj1
            obj1.save()
            obj2.save()
            send_mail(
                subject='Welcome to Excel International School of Studies!',
                message=f'Hi {username}, your staff account has been created successfully. Please checkout the official EXCEL SCHOOL RECORD site. USERNAME: {username}, PASSWORD: {password}.  Thank You!',
                from_email='malavikamanoj4@gmail.com',
                recipient_list=[email]
            )
            print('sent')

            return redirect('admin_page')        
        else:
            context={ 
                'form1': form1,
                'form2': form2
            }
            return render(request,'admin/staff_signup.html', context=context)
        
def staff_in_detail(request,id):
    staff=StaffDetail.objects.get(pk=id)
    context={}
    context['data']=staff
    return render(request,'admin/staff_in_detail.html',context=context)

def update_staff_detail(request, id):
    
    staff=StaffDetail.objects.get(pk=id)
    if request.method=='GET':
        
        context={
            'form1': UserEditForm(instance=staff.staff_name),
            'form2': StaffDetailForm(instance=staff)
            }
        
        return render(request,'admin/staff_signup.html',context)
    elif request.method=='POST':
        user1=UserEditForm(request.POST,request.FILES, instance=staff.staff_name)
        staff1=StaffDetailForm(request.POST,instance=staff)
        if user1.is_valid() and staff1.is_valid():
            obj1=user1.save(commit=False)
            obj2=staff1.save(commit=False)
            obj2.staff_name=obj1
            obj1.save()
            obj2.save()
            return redirect('admin_page')
        else:
            context={
                'form1': user1,
                'form2': staff1
            }
            return render(request, 'admin/staff_signup.html', context)
    
def add_subject(request):
    if request.method=='GET':
        context={
            'form': SubjectForm()
        }
        return render(request,'admin/add_subject.html', context=context)
    elif request.method=='POST':
        form=SubjectForm(request.POST)

        if form.is_valid():
            obj1=form.save()
            obj1.save()

            return redirect('add_subject')        
        else:
            context={ 
                'form': form
            }
            return render(request,'admin/add_subject.html', context=context)
        
def teacher_student_list(request,a_id):
    if request.method=='GET':

        teacher=StaffDetail.objects.get(pk=a_id)
        context={}
        context['data']=Student_data.objects.filter(teacher=teacher)
        return render(request,'admin/student_list.html',context=context)
    elif request.method=='POST':
        term=request.POST['term']
        s_id=request.POST['s_id']
        lst = MarkList.objects.filter(term=term,student_id=s_id) 
        if len(lst)>0:
            return redirect('student_marklist',term=term,s_id=s_id)
        return redirect('teacher_student_list', a_id=a_id)