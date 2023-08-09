from django.shortcuts import render,redirect
from staff.models import Student_data
from admin.models import Subject
from .models import MarkList
from staff.views import find_grade
from django.core.mail import send_mail

# Create your views here.
def student_profile(request):
    student=Student_data.objects.get(student=request.user)
    context={}
    context['data']=student
    return render(request,'student/student_profile.html',context=context)

# def student_home(request):
#     return render(request, 'student/shared/base.html')

def student_progress_card(request):
    student=Student_data.objects.get(student=request.user)
    data = []
    # student = Student_data.objects.get(id=s_id) 
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
    return render(request,'student/progress_card.html', context=context)









