from django.shortcuts import render,redirect
from admin.forms import *
from .forms import *
from django.core.mail import send_mail
# Create your views here.

def staff_profile(request):
    staff=StaffDetail.objects.get(staff_name=request.user)
    context={}
    context['data']=staff
    return render(request,'staff/staff_profile.html',context=context)

def student_signup(request):
    if request.method=='GET':
        context={
            'form1': UserForm(),
            'form2': Student_dataForm(),
            'form3': ParentDetailForm(),
        }

        return render(request,'staff/student_form.html', context=context)
    elif request.method=='POST':
        form1=UserForm(request.POST,request.FILES)
        form2=Student_dataForm(request.POST)
        form3=ParentDetailForm(request.POST)
        staff=StaffDetail.objects.get(staff_name=request.user)
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            email=request.POST.get('email')
            obj1=form1.save(commit=False)
            obj2=form2.save(commit=False)
            obj3=form3.save(commit=False)
            obj1.set_password(form1.cleaned_data['password'])
            obj2.student=obj1
            obj2.parent=obj3
            obj2.standard=staff.class_taught
            obj2.teacher=staff
            obj1.save()
            obj3.save()
            obj2.save()
            
            send_mail(
                subject='Welcome to Excel International School of Studies!',
                message=f'Hi {username}, your student account has been created successfully. Please checkout the official EXCEL SCHOOL RECORD site. USERNAME: {username}, PASSWORD: {password}.  Thank You!',
                from_email='malavikamanoj4@gmail.com',
                recipient_list=[email]
            )
            print('sent')

            return redirect('student_list')        
        else:
            context={ 
                'form1': form1,
                'form2': form2
            }
            return render(request,'staff/student_form.html', context=context)

def student_list(request):
    if request.method=='GET':

        teacher=StaffDetail.objects.get(staff_name=request.user)
        context={}
        context['data']=Student_data.objects.filter(teacher=teacher)
        return render(request,'staff/student_list.html',context=context)
    elif request.method=='POST':
        term=request.POST['term']
        s_id=request.POST['s_id']
        lst = MarkList.objects.filter(term=term,student_id=s_id) 
        if len(lst)>0:
            return redirect('student_marklist',term=term,s_id=s_id)
        return redirect('student_list')
    
def student_detail(request,id):
    student=Student_data.objects.get(pk=id)
    context={}
    context['data']=student
    return render(request,'staff/student_detail.html',context=context)

def update_student_detail(request,id):
    student=Student_data.objects.get(pk=id)
    if request.method=='GET':
        
        context={
            'form1': UserEditForm(instance=student.student),
            'form2': Student_dataForm(instance=student),
            'form3': ParentDetailForm(instance=student.parent),

            }
        
        return render(request,'staff/student_form.html',context)
    elif request.method=='POST':
        user1=UserEditForm(request.POST,request.FILES, instance=student.student)
        stud1=Student_dataForm(request.POST,instance=student)
        parent1=ParentDetailForm(request.POST, instance=student.parent)
        staff=StaffDetail.objects.get(staff_name=request.user)

        if user1.is_valid() and stud1.is_valid() and parent1.is_valid():
            obj1=user1.save(commit=False)
            obj2=stud1.save(commit=False)
            obj3=parent1.save(commit=False)
            obj2.student=obj1
            obj2.parent=obj3
            obj2.standard=staff.class_taught
            obj1.save()
            obj3.save()
            obj2.save()
            return redirect('student_list')
        else:
            context={
                'form1': user1,
                'form2': stud1,
                'form3': parent1
            }
            return render(request, 'staff/student_form.html', context)
        
def staff_home(request):
    return render(request,'accounts/shared/base.html')

def student_mark_form(request,id):
    student=Student_data.objects.get(pk=id)
    staff=StaffDetail.objects.get(staff_name=request.user)
    print(staff.class_taught_id)
    sub = Subject.objects.filter(standard_id=staff.class_taught_id)
    print(sub)

    if request.method=='GET':
        context={
            'form': MarkListForm(),
            'subject': sub,
        }

        return render(request,'staff/student_mark_form.html', context=context)
    elif request.method=='POST':
        i = 1
        for s in sub:
            obm = request.POST[f'obm{i}']
            maxm = request.POST[f'maxm{i}']
            term=request.POST['term']
            MarkList.objects.create(student=student,subject=s,marks_obtained=obm, max_marks=maxm,term=term)
            i+=1
        return redirect('student_list')

def find_grade(m,t):
    try:
        p=(m/t)*100
        if p>=90:
            grade="A1"
        elif p>=80:
            grade="A"
        elif p>=70:
            grade="B1"
        elif p>=60:
            grade="B"
        elif p>=50:
            grade="C1"
        elif p>=40:
            grade="C"
        elif p>=30:
            grade="D1"
        elif p>=20:
            grade="D"
        else:
            grade="E"
        return grade,"%.2f" %p
        
    except:
         0

def student_marklist(request,s_id,term):
    mark_list = MarkList.objects.filter(student_id=s_id,term=term)
    c = 1
    total_mark = 0
    total_max_mark = 0
    data = []
    for mark in mark_list:
        temp = {}
        temp['mark'] = mark
        total_mark += mark.marks_obtained
        total_max_mark += mark.max_marks
        sub_grade=find_grade(mark.marks_obtained,mark.max_marks)
        temp['grade'] = sub_grade
        data.append(temp)
        c+=1
        
    overall_grade=find_grade(total_mark,total_max_mark)
    
    context={}
    context['data'] = data
    context['term'] = term
    context['total_mark'] = total_mark
    context['total_max_mark'] = total_max_mark
    # context['percentage'] = percentage    
    context['overall_grade']= overall_grade
    return render(request,'staff/student_marklist.html', context=context)

def progress_card(request,s_id):
    data = []
    student = Student_data.objects.get(id=s_id) 
    subjects = Subject.objects.filter(standard=student.standard)
    total_mark=[0,0,0]
    total_max_mark=[0,0,0]
    tmp=[]
    tot_m=[]
    for subject in subjects:
        temp_dict = {}
        temp_list = []
        

        for i in range(3):
            try:
                mark = MarkList.objects.get(student=student,subject=subject,term=i+1)
                temp_list.append((mark, find_grade(mark.marks_obtained, mark.max_marks)))
                
                total_mark[i] += mark.marks_obtained
                total_max_mark[i] += mark.max_marks
                
                
            except:
                temp_list.append(0)
        temp_dict['sub'] = subject
        temp_dict['mark'] = temp_list
        data.append(temp_dict)
    grand_total=0
    grand_max_total=0
    for i in range(3):
        tmp.append(find_grade(total_mark[i],total_max_mark[i]))
        grand_total +=total_mark[i]
        grand_max_total += total_max_mark[i]
    tot_m.append(find_grade(grand_total,grand_max_total))
    print(total_mark)
    print(tmp)
    context = {}
    context['student'] = student
    context['data'] = data
    context['total_mark']=total_mark
    context['total_max_mark']= total_max_mark
    context['grade']=tmp
    context['overall']=tot_m
    context['grand_total']=grand_total
    context['grand_max_total']=grand_max_total
    return render(request,'staff/progress_report.html', context=context)

def send_progress_card(request, t_id):
    parent_mail=Student_data.objects.filter(teacher_id=t_id).values_list('parent__parent_email')
    em = []
    for i in parent_mail:
        em.append(i[0])
    send_mail(
        subject='Information from Excel International School',
        message=f"Dear Parent, Your child's Termly progress report is ready. Please checkout the progress card of your child by loging in our offical website. Thank You!",
        from_email='malavikamanoj4@gmail.com',
        recipient_list=em
    )
    return redirect('student_list')