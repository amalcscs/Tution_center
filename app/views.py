import os
import random
from django.shortcuts import render, redirect
from app.models import *
from datetime import datetime,date
from django.http import HttpResponse, HttpResponseRedirect
from django. contrib import messages
from django.conf import settings
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from Tution_center.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


def login(request):
    manager = designation.objects.get(designation="manager")
    staff = designation.objects.get(designation="staff")
    student = designation.objects.get(designation="student")
    account = designation.objects.get(designation="account")
    
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'Admin_dashboard')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=manager.id,status="active").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['m_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['m_id'] = member.id 
                man=user_registration.objects.filter(id= member.id)
                
                return render(request,'MAN_profile.html',{'man':man})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=staff.id,status="active").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['stf_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['stf_id'] = member.id 
                mem=user_registration.objects.filter(id= member.id)
                
                return render(request,'Staff_dashboard.html',{'mem':mem})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=student.id,status="active").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['usernamets1'] = member.designation_id
                request.session['std_id'] = member.id 
                mem1=user_registration.objects.filter(id= member.id)
                
                return render(request,'Student_profiledash.html',{'mem1':mem1})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=account.id,status="active").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['acc_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['acc_id'] = member.id 
                acc=user_registration.objects.filter(id= member.id)
                
                return render(request,'account_dashboard.html',{'acc':acc})
    
        else:
            context = {'msg_error': 'Invalid data'}
            return render(request, 'login.html', context)

       
    return render(request,'login.html')


def reset_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        access_user_data = user_registration.objects.filter(email=email).exists()
        if access_user_data:
            user = user_registration.objects.get(email=email)
            password = random.SystemRandom().randint(100000, 999999)

            user.password = password

            user.save()
            subject = 'Tuition Centre your authentication data updated\n'
            message = 'Password Reset Successfully\n\nYour login details are below\n\nUsername : ' + str(email) + '\n\nPassword : ' + str(password) + \
                '\n\nYou can login this details'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email, ]
            send_mail(subject, message, email_from,
                      recipient_list, fail_silently=False)
            msg_success = "Password Reset successfully check your mail new password"
            return render(request, 'Reset_password.html', {'msg_success': msg_success})
        else:
            msg_error = "This email does not exist iNFOX Technologies "
            return render(request, 'Reset_password.html', {'msg_error': msg_error})

    return render(request,'Reset_password.html')


def Registration_form(request):
    bat = batch.objects.all()
    a = user_registration()
    if request.method == 'POST':
        a.fullname = request.POST['fname']
        a.fathername = request.POST['fathername']
        a.mothername = request.POST['mothername']
        a.dateofbirth = request.POST['dob']
        a.gender = request.POST['gender']
        a.presentaddress1 = request.POST['address1']
        a.presentaddress2  =  request.POST['address2']
        a.presentaddress3 =  request.POST['address3']
        a.pincode = request.POST['pincode']
        a.district  =  request.POST['district']
        a.state  =  request.POST['state']
        a.country  =  request.POST['country']
        a.permanentaddress1 = request.POST['paddress1']
        a.permanentaddress2  =  request.POST['paddress2']
        a.permanentaddress3  =  request.POST['paddress3']
        a.permanentpincode = request.POST['ppincode']
        a.permanentdistrict  =  request.POST['pdistrict']
        a.permanentstate  =  request.POST['pstate']
        a.permanentcountry =  request.POST['pcountry']
        a.mobile = request.POST['mobile']
        a.alternativeno = request.POST['alternative']
        a.batch_id = request.POST['batch']
        a.email = request.POST['email']
        a.password = random.randint(10000, 99999)
        # a.designation_id = des.id
        # a.password= random.SystemRandom().randint(100000, 999999)
        
        #a.branch_id = request.POST['branch']
        a.photo = request.FILES['photo']
        a.idproof = request.FILES['idproof']
        a.save()
        
        x = user_registration.objects.get(id=a.id)
        today = date.today()
        tim = today.strftime("%m%y")
        x.employee_id = "INF"+str(tim)+''+"B"+str(x.id)
        passw=x.password
        email_id=x.email
        x.save()
        y1 = user_registration.objects.get(id=a.id)
        subject = 'Welcome Tuition Centre'
        message = 'Congratulations,\n' \
        'You have successfully registered with our website.\n' \
        'username :'+str(a.email)+'\n' 'password :'+str(a.password) + \
        '\n' 'WELCOME '
        recepient = str(a.email)
        send_mail(subject, message, EMAIL_HOST_USER,
                [recepient], fail_silently=False)
        msg_success = "Registration successfully Check Your Registered Mail"
        
        return render(request, 'Registration_form.html',{'msg_success': msg_success,'bat':bat})
    return render(request, 'Registration_form.html',{'bat':bat})


def Staff_logout(request):
    if 'stf_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

#********************************Staff module************************
#********************************Amal************************

def Staff_index(request):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=stf_id)
        return render(request,'Staff_index.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_accsetting(request):
    if 'stf_id' in request.session:
        
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=stf_id)
        return render(request,'Staff_accsetting.html', {'mem': mem})
    else:
        return redirect('/')

def Staff_accsettingimagechange(request,id):
    if 'stf_id' in request.session:
        
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=stf_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('Staff_accsetting')
        return render(request, 'Staff_accsetting.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_changepwd(request):
    
    if 'stf_id' in request.session:
        
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']     
        mem = user_registration.objects.filter(id=stf_id)   
          
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            cur = abc.password
            oldps = request.POST["currentPassword"]
            newps = request.POST["newPassword"]
            cmps = request.POST["confirmPassword"]
            if oldps == cur:
                if oldps != newps:
                    if newps == cmps:
                        abc.password = request.POST.get('confirmPassword')
                        abc.save()
                        return render(request, 'Staff_dashboard.html', {'mem': mem})
                elif oldps == newps:
                    messages.add_message(request, messages.INFO, 'Current and New password same')
                else:
                    messages.info(request, 'Incorrect password same')

                return render(request, 'Staff_dashboard.html', {'mem': mem})
            else:
                messages.add_message(request, messages.INFO, 'old password wrong')
                return render(request, 'Staff_changepwd.html', {'mem': mem})
        return render(request, 'Staff_changepwd.html', {'mem': mem})
                 
    else:
        return redirect('/')

def Staff_dashboard(request):
    if 'stf_id' in request.session:
        
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=stf_id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=stf_id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
            return render(request,'Staff_dashboard.html', {'labels':labels,'data':data,'mem': mem})
    else:
        return redirect('/')

def Staff_attendance(request):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=stf_id)
        return render(request, 'Staff_attendance.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_attendancesort(request):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=stf_id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=stf_id)
        return render(request, 'Staff_attendancesort.html',{'mem1':mem1,'mem':mem})
    else:
        return redirect('/')
    

def Staff_reportissues(request):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=stf_id)
        return render(request,'Staff_reportissues.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_reportedissue(request):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=stf_id)
        var=reported_issue.objects.filter(reporter_id=stf_id).order_by("-id")
        return render(request,'Staff_reportedissue.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_reportanissue(request):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=stf_id)
        ad_id = designation.objects.get(designation="manager")
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('report')
            vars.reported_date=datetime.now()
            vars.reported_to_id=ad_id.id
            vars.reporter_id=stf_id
            vars.status='pending'
            vars.save()
            return redirect('Staff_reportissues')
        else:
             return render(request,'Staff_reportanissue.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_issuereportsstudents(request):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=stf_id)
        var=reported_issue.objects.filter(reported_to_id=stf_id).order_by("-id")
        return render(request,'Staff_issuereportsstudents.html',{'mem':mem,'var':var})
    else:
            return redirect('/')

def Staffreplyview(request,id):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=stf_id)
        rid=request.GET.get('rid')
        mem1=reported_issue.objects.filter(id=id)
        
        return render(request, 'Staffreplyview.html',{'mem1':mem1,'mem':mem})
    else:
        return redirect('/')

def Staffissuereply(request,id):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            return redirect('/')
        stf_id = user_registration.objects.filter(id=stf_id)
        if request.method == 'POST':
            v = reported_issue.objects.get(id=id)
            v.reply=request.POST.get('reply')
            v.save()
        return redirect('Staff_reportissues')

    else:
        return redirect('/')

#********************************Subeesh*********************************

def Staff_leave(request):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        if request.session.has_key('usernametrns2'):
            usernametrns2 = request.session['usernametrns2']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=stf_id)
        
        return render(request, 'Staff_leave.html',{'mem':mem})
    

def Staff_Student_det(request):
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=stf_id)
        return render(request,'Staff_Student_det.html',{'mem':mem})

def Staff_apply_leave(request):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=stf_id)
        pro2 = designation.objects.get(designation="staff")
        if request.method == "POST":
            
            
            me = Leave()
            me.from_date = request.POST.get('from')
            me.to_date = request.POST.get('to')
            me.leave_status = request.POST.get('haful')
            me.reason = request.POST.get('reason')
            me.user_id = stf_id
            me.designation_id = pro2.id
            me.status = "pending"
            me.save()
        return render(request, 'Staff_apply_leave.html',{'mem':mem})

def Staff_Req_leave(request):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=stf_id)
        var = Leave.objects.filter(user_id=stf_id).order_by("-id")
    return render(request, 'Staff_Req_leave.html',{'mem':mem,'var':var})

# def Student_profiledash(request):
#     return render(request, 'Student_profiledash.html')


def Staff_studentsleave_table(request):
    if 'stf_id' in request.session:
        if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
        else:
            variable="dummy"
        mem = user_registration.objects.filter(id=stf_id)
        des = designation.objects.get(designation='student')
        sl = Leave.objects.filter(designation_id=des.id).all().order_by('-id')
        return render(request, 'Staff_studentsleave_table.html',{'sl': sl,'mem':mem})


def Staff_current_students(request):
    if request.session.has_key('stf_id'):
        stf_id = request.session['stf_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=stf_id)
    des = designation.objects.get(designation='student')
    cs = user_registration.objects.filter(status='active').filter(designation_id=des).order_by('-id')
    
    return render(request, 'Staff_current_students.html',{'cs': cs,'mem':mem})

def Staff_student_dashboard(request,id):
    if request.session.has_key('stf_id'):
        stf_id = request.session['stf_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=stf_id)
    csd=user_registration.objects.filter(id=id)
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=id)
    for i in queryset:
        labels=[i.workperformance,i.attitude,i.creativity]
        
        
        data=[i.workperformance,i.attitude,i.creativity]
    return render(request, 'Staff_student_dashboard.html',{'labels':labels,'data':data,'csd':csd,'mem':mem})


def Staff_previous_students(request):
    if request.session.has_key('stf_id'):
        stf_id = request.session['stf_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=stf_id)
    # csd=user_registration.objects.filter(id=id)
    des = designation.objects.get(designation='student')
    ps = user_registration.objects.filter(status='resign').filter(designation_id=des).order_by('-id')
    return render(request, 'Staff_previous_students.html',{'ps': ps,'mem':mem})

def Staff_previous_student_dashboard(request,id):
    if request.session.has_key('stf_id'):
        stf_id = request.session['stf_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=stf_id)
    psd=user_registration.objects.filter(id=id)
    return render(request, 'Staff_previous_student_dashboard.html',{'psd':psd,'mem':mem})


def Staff_progress_report(request):
    if request.session.has_key('stf_id'):
        stf_id = request.session['stf_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=stf_id)
    desi = designation.objects.get(designation='student')
    sps = user_registration.objects.filter(designation_id=desi).filter(status='active')
    return render(request, 'Staff_progress_report.html',{'desi':desi,'sps': sps,'mem':mem})

def Staff_progress_report_add(request):
    if request.method == 'POST':
        fn1 = request.POST['sname']
        fn2 = request.POST['ssubject']
        fn3 = request.POST['smark']
        fn4 = request.POST['sdate']
        
        
        students = user_registration.objects.get(fullname=fn1)
        
        new2 = progressreport(user=students, subject=fn2, mark=fn3, date=fn4)
        new2.save()
    return redirect('Staff_progress_report_show')
    



def Staff_progress_report_show(request):
    if request.session.has_key('stf_id'):
            stf_id = request.session['stf_id']
    else:
        variable="dummy"
    mem = user_registration.objects.filter(id=stf_id)
    desi = designation.objects.get(designation='student')
    pr=progressreport.objects.all()
    sps = user_registration.objects.filter(designation_id=desi).filter(status='active')
    
    return render(request, 'Staff_progresss_report.html',{'pr':pr,'sps':sps,'mem':mem})



def Staff_rejected_leave(request,id):
    if request.method == 'POST':
        staff_reason=request.POST.get('reply')
        pro_sts = Leave.objects.filter(id=id).update(leave_rejected_reason= staff_reason,status ='Rejected')
        
       
    return redirect('Staff_studentsleave_table')


def Staff_accepted_leave(request,id):
    
    al = Leave.objects.filter(id=id).update(status ='Approved')
        
       
    return redirect('Staff_studentsleave_table')




    #************************Student module**************************
 #************************Anwar**************************

def Student_index(request):
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
    mem1 = user_registration.objects.filter(id=std_id)  
    return render(request, 'Student_index.html',{'mem1':mem1})

def Student_logout(request):
    if 'std_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def Student_profiledash(request):
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
    mem1 = user_registration.objects.filter(id=std_id)

    student=user_registration.objects.all()
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=std_id)
    for i in queryset:
        labels=[i.workperformance,i.attitude,i.creativity]
        
        
        data=[i.workperformance,i.attitude,i.creativity]
    return render(request, 'Student_profiledash.html',{'labels':labels,'data':data,'user_registration':student,'mem1':mem1})

def Student_attendance(request):
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
    mem1 = user_registration.objects.filter(id=std_id) 
    return render(request, 'Student_attendance.html',{'mem1':mem1})

def Student_attendancesort(request):
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
    mem1 = user_registration.objects.filter(id=std_id) 

    if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=std_id)
    return render(request, 'Student_attendancesort.html',{'mem1':mem1,'adata':adata})


def Student_reportissues(request):
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
    mem1 = user_registration.objects.filter(id=std_id)
    return render(request, 'Student_reportissues.html',{'mem1':mem1})


def Student_leaverejected(request,id):
    if 'std_id' in request.session:
        if request.session.has_key('std_id'):
            std_id = request.session['std_id']
        else:
            variable="dummy"
        mem1 = user_registration.objects.filter(id=std_id)
        var = Leave.objects.get(id=id)
        return render(request,'Student_leaverejected.html',{'mem1':mem1,'var':var}) 
    else:
        return redirect('/')


def Studentreportsuccess(request):
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
        mem1 = user_registration.objects.filter(id=std_id)

        mem11 = user_registration.objects.get(id=std_id)
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('report')
            vars.reported_date=datetime.now()
            vars.reporter_id=std_id
            vars.status='pending'
            vars.save()
        return render(request, 'Student_reportissues.html',{'mem1':mem1})
    else:
        return redirect('/')


def Student_reportissue1(request):
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
    mem1 = user_registration.objects.filter(id=std_id)

    var=reported_issue.objects.filter(reporter_id=std_id).order_by("-id") 
    return render(request, 'Student_reportissue1.html',{'mem1':mem1,'var':var})

def Student_reportissue2(request):
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
    mem1 = user_registration.objects.filter(id=std_id) 
    return render(request, 'Student_reportissue2.html',{'mem1':mem1})

def Student_reportissuereply(request,id):
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
    mem1 = user_registration.objects.filter(id=std_id) 
    var=reported_issue.objects.filter(id=id)
    return render(request, 'Student_reportissuereply.html',{'mem1':mem1,'var':var})

def Student_accsetting(request):
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
    else:
        return redirect('/')
    mem1 = user_registration.objects.filter(id=std_id) 
    return render(request,'Student_accsetting.html', {'mem1': mem1})
    

def Student_accsettingimagechange(request,id):
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
        mem1 = user_registration.objects.filter(id=std_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('Student_accsetting')
        return render(request, 'Student_accsetting.html',{'mem1':mem1})
    else:
        return redirect('/')

def Student_changepwd(request):
    
    if request.session.has_key('std_id'):
        std_id = request.session['std_id']
        mem1 = user_registration.objects.filter(id=std_id) 
          
        if request.method == 'POST':
            abc = user_registration.objects.get(id=std_id)
            cur = abc.password
            oldps = request.POST["currentPassword"]
            newps = request.POST["newPassword"]
            cmps = request.POST["confirmPassword"]
            if oldps == cur:
                if oldps != newps:
                    if newps == cmps:
                        abc.password = request.POST.get('confirmPassword')
                        abc.save()
                        return render(request, 'Student_profiledash.html', {'mem1': mem1})
                elif oldps == newps:
                    messages.add_message(request, messages.INFO, 'Current and New password same')
                else:
                    messages.info(request, 'Incorrect password same')

                return render(request, 'Student_changepwd.html', {'mem1': mem1})
            else:
                messages.add_message(request, messages.INFO, 'old password wrong')
                return render(request, 'Student_changepwd.html', {'mem1': mem1})
        return render(request, 'Student_changepwd.html', {'mem1': mem1})
                 
    else:
        return redirect('/')

def Student_applyleave_cards(request):
    if 'std_id' in request.session:
        if request.session.has_key('std_id'):
            std_id = request.session['std_id']
        if request.session.has_key('usernametrns1'):
            usernametrns1 = request.session['usernametrns1']
        else:
            variable="dummy"
        mem1 = user_registration.objects.filter(id=std_id)
    return render(request,'Student_applyleave_cards.html',{'mem1':mem1})

def Student_leavereq(request):
    if 'std_id' in request.session:
        if request.session.has_key('std_id'):
            std_id = request.session['std_id']
        if request.session.has_key('usernamets1'):
            usernamets1 = request.session['usernamets1']
        else:
            variable="dummy"
        mem1 = user_registration.objects.filter(id=std_id)
        pro2 = user_registration.objects.get(id=std_id)
        pro3=designation.objects.get(designation="student")
        if request.method == "POST":
            
            
            mem = Leave()
            mem.from_date = request.POST.get('from')
            mem.to_date = request.POST.get('to')
            mem.leave_status = request.POST.get('haful')
            mem.reason = request.POST.get('reason')
            mem.user_id = std_id
            mem.designation_id = pro3.id
            mem.status = "pending"
            mem.save()
        return render(request,'Student_leavereq.html', {'mem1':mem1})
    

def Student_reqedleave(request):
    if 'std_id' in request.session:
        if request.session.has_key('std_id'):
            std_id = request.session['std_id']
        else:
            variable="dummy"
        mem1 = user_registration.objects.filter(id=std_id)
        var = Leave.objects.filter(user_id=std_id).order_by('-id')
        return render(request, 'Student_reqedleave.html',{'mem1':mem1,'var':var}) 
    else:
        return redirect('/')

def Student_progressreport(request):
    if 'std_id' in request.session:
        if request.session.has_key('std_id'):
            std_id = request.session['std_id']
        else:
            variable="dummy"
        mem1 = user_registration.objects.filter(id=std_id)
        progress = progressreport.objects.filter(user_id=std_id)
        return render(request,'Student_progressreport.html',{'mem1':mem1, 'progressreport':progress})

    #************************Manager module**************************


#************************Anwar**************************

def Man_index(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)  
    return render(request, 'Man_index.html',{'man':man})

def Man_logout(request):
    if 'm_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')


def man_page1(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id) 
 
    bach=batch.objects.all()
    dsg=designation.objects.all()
    userreg=user_registration.objects.all()
    return render(request,'Man_attendance.html', {'man':man,'batch':bach,'designation':dsg,'user_registration':userreg})  


def man_page3(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id) 
 
    if request.method == "POST":
        empname1=request.POST.get('empname')
        atten=attendance.objects.filter(user_id=empname1)
        return render(request,'Man_attendanceshow.html',{'man':man,'atten':atten,'empname1':empname1}) 

    
def man_desi(request):   
    dept_id = request.GET.get('dept_id')
    bach=batch.objects.all()
    Desig = designation.objects.filter(~Q(designation="manager"))
    return render(request, 'Man_designation.html', {'Desig': Desig,'batch':bach})


def man_emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    dept=batch.objects.filter(id=dept_id)
    desi=designation.objects.filter(id=desig_id)
    user=user_registration.objects.filter(designation_id=desig_id).filter(batch_id=dept_id)
    print(dept)
    print(desi)
    print(user)
    return render(request, 'Man_employee.html',{'user':user,'dept':dept,'desi':desi})

    
#*******************Nimisha**************************

def MAN_Academic(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"  
        man = user_registration.objects.filter(id=m_id)
        ba = batch.objects.all()
        var = class_registration.objects.all()
        return render(request,'MAN_Academic.html',{'ba':ba,'var':var,'man':man})
    else:
        return redirect('/') 


def MAN_UpdateClass(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"  
        man = user_registration.objects.filter(id=m_id) 
        var= class_registration.objects.filter(id=id)
        vars=class_registration.objects.get(id=id)
        ba = batch.objects.all()
        return render(request,'MAN_UpdateClass.html',{'ba':ba,'var':var,'vars':vars,'man':man})
    else:
        return redirect('/') 


def MAN_Update_Classsave(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"  
        man = user_registration.objects.filter(id=m_id)  
        if request.method == 'POST':
            var = class_registration.objects.get(id=id)
            var.class_name= request.POST.get('class')
            var.description = request.POST.get('discrip')
            var.batch_name_id = request.POST.get('batch')
            var.save()
            # m="Class updated Successfully"
        return render(request,'MAN_UpdateClass.html',{'man':man})
    else:
        return redirect('/') 



def MAN_deleteclass(request,id):
    
        m = class_registration.objects.get(id=id)
        m.delete()
        return redirect('MAN_ViewClass')
    

def MAN_ViewClass(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"  
        man = user_registration.objects.filter(id=m_id)  
        var =class_registration.objects.all()
        batch_id = request.GET.get('batch_id ')
        ba=batch.objects.filter(batch=batch_id)
        return render(request,'MAN_ViewClass.html',{'var':var,'ba':ba,'man':man})
    else:
        return redirect('/') 


#******************************************Meenu************************

def Manager_staff(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        return render(request,'Manager_staff.html',{'man':man})

def Manager_currentstaffdetails(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        data = designation.objects.get(designation='staff')
        names =user_registration.objects.filter(status='active').filter(designation=data)
        return render(request,'Manager_currentstaffdetails.html',{'names':names,'man':man})

def Manager_previousstaffdetails(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        data1= designation.objects.get(designation='staff')
        details =user_registration.objects.filter(status='resign').filter(designation=data1)
        return render(request,'Manager_previousstaffdetails.html',{'details':details,'man':man})

def Manager_staffprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id) 
        prodata = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'Manager_staffprofile.html',{'labels':labels,'data':data,'man':man,'prodata':prodata})


def Manager_attendancesearch(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id) 
        id = id
        return render(request,'Manager_attendancesearch.html',{'man':man,'id':id})



def Manager_attendancesort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        id=id
        if request.method == "POST":
            fromdate = request.POST.get('from')
            todate = request.POST.get('to') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request,'Manager_attendancesort.html',{'man':man,'mem1':mem1,'id':id})
    else:
        return redirect('/')

 
#------------------Student-----------------#

def Manager_student(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id) 
        return render(request,'Manager_student.html',{'man':man})

def Manager_currentstudentdetails(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id) 
        stud_data = designation.objects.get(designation='student')
        studname =user_registration.objects.filter(status='active').filter(designation=stud_data)
        return render(request,'Manager_currentstudentdetails.html',{'studname':studname,'man':man})

def Manager_previousstudentdetails(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        data1= designation.objects.get(designation='student')
        details =user_registration.objects.filter(status='resign').filter(designation=data1)
        return render(request,'Manager_previousstudentdetails.html',{'details':details,'man':man})

def Manager_studentprofile(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        prodata1 = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'Manager_studentprofile.html',{'labels':labels,'data':data,'man':man,'prodata1':prodata1})


def Manager_student_attendancesearch(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        id = id
        return render(request,'Manager_studentattendancesearch.html',{'man':man,'id':id})


def Manager_sort(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id) 
        id = id
        if request.method == "POST":
            fromdate = request.POST.get('from')
            todate = request.POST.get('to') 
            mem2 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request,'Manager_studentattendancesort.html',{'man':man,'mem2':mem2,'id':id})

#------------Leave Request------------#

def Manager_leaverequest_staff(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id) 
        return render(request,'Manager_leaverequest_staff.html',{'man':man})



def Manager_apply_leave(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id) 
        mem3 = designation.objects.get(designation='manager') 
        if request.method == "POST":
            mem1 = Leave()
            mem1.from_date = request.POST.get('from')
            mem1.to_date = request.POST.get('to')
            mem1.leave_status = request.POST.get('haful')
            mem1.reason = request.POST.get('reason')
            mem1.user_id = m_id
            mem1.designation_id = mem3.id
            mem1.status = "pending"
            mem1.save()
        return render(request, 'Manager_applyleave.html',{'man':man})
    else:
        return redirect('/')



def Manager_requestleave(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        newdata = Leave.objects.filter(designation_id=m_id).order_by("-id")
        return render(request,'Manager_requestleave.html',{'man':man,'newdata':newdata})
    
def Manager_staffleave(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        Man = designation.objects.get(designation='staff')
        sl= Leave.objects.filter(designation_id=Man.id).all().order_by('-id')
        return render(request,'Manager_staffleave.html',{'man':man,'sl':sl})


def Manager_rejected_leave(request,id):
    if request.method == 'POST':
        staff_reason=request.POST.get('reply')
        pro_sts = Leave.objects.filter(id=id).update(leave_rejected_reason= staff_reason,status ='Rejected')
    return redirect('Manager_staffleave')


def Manager_accepted_leave(request,id):
    al = Leave.objects.filter(id=id).update(status ='Approved')
    return redirect('Manager_staffleave')


#------------------Academics-----------------#

def Manager_academics(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id) 
        return render(request,'Manager_academics.html',{'man':man})


def Manager_academics_viewbatch(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        var = batch.objects.all()
        return render(request,'Manager_academics_viewbatch.html',{'man':man,'var':var})


def Manager_academics_update(request,id):
   if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        var= batch.objects.filter(id=id)
        vars=batch.objects.get(id=id)
        ba = batch.objects.all()
        return render(request,'Manager_academics_update.html',{'man':man,'ba':ba,'var':var,'vars':vars})


def Manager_academics_updatesave(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            var = batch.objects.get(id=id)
            var.batch= request.POST.get('batchname')
            var.description= request.POST.get('desc')
            var.save()
            m="Updated successfully"
        return render(request,'Manager_academics_update.html',{'man':man,'m':m})


def Manager_academics_delete(request,id):
    var = batch.objects.get(id=id)
    var.delete()
    return redirect('/Manager_academics_viewbatch')

#********************Akhil***************************************

def MAN_Report(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        des = designation.objects.all()
        # filter(~Q("admin"))
        return render(request,'MAN_Report.html',{'des':des,'man':man })

# def MAN_Reportedissue(request):
#     des = designation.objects.all()
#     return render(request,'MAN_Reportedissue.html',{'des':des })

def MAN_ReportedissueShow(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        designations=designation.objects.get(id=id)
        user=user_registration.objects.filter(designation_id=id)
        reported_issues=reported_issue.objects.all()
        return render(request,'MAN_ReportedissueShow.html',{'man':man,'designation':designations,'reported_issue':reported_issues,'user_registration':user})

def MAN_rep(request,id):
    
        if request.method == 'POST':
            
            vars = reported_issue.objects.get(id=id)
            vars.reply=request.POST.get('reply')
            vars.status='submitted'
            vars.save()
           
            return redirect('MAN_Report')
       

def MAN_ReportedissueShow1(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'MAN_ReportedissueShow1.html',{'man':man,'reported_issue':reported_issues})


def MAN_manager_report(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_manager_report.html',{'man':man})

def MAN_Reportissue(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable ="dummy"
        man = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_Reportissue.html',{'man':man})

def MAN_reportsuccess(request):
    if 'mnid' in request.session:
        if request.session.has_key('mnid'):
            mnid = request.session['mnid']
        else:
            variable="dummy"
        pro = user_registration.objects.filter(id=mnid)
        design=designation.objects.get(designation="admin")
        man = user_registration.objects.get(designation_id=design.id)
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('MANreportissue')
            vars.reported_date=datetime.now()
            vars.reported_to_id=man.id
            vars.reporter_id=mnid
            vars.status='pending'
            vars.save()
        return render(request, 'MAN_Reportissue.html',{'pro':pro})
    else:
        return redirect('/')
    

def MAN_manger_reportedissues(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        man = user_registration.objects.filter(id=m_id)
        var = reported_issue.objects.filter(reporter=m_id)
        return render(request,'MAN_manger_reportedissues.html',{'var':var,'man':man})


def MAN_manger_reportedissues1(request,id):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        man = user_registration.objects.filter(id=m_id)
        reported_issues=reported_issue.objects.get(id=id)
        return render(request,'MAN_manger_reportedissues1.html',{'reported_issue':reported_issues,'man':man})
    
#*******************************sharon**********************************

def MAN_profile(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id) 
    labels = []
    data = []
    queryset = user_registration.objects.filter(id=m_id)
    for i in queryset:
        labels=[i.workperformance,i.attitude,i.creativity]
        
        
        data=[i.workperformance,i.attitude,i.creativity]
    return render(request, 'MAN_profile.html',{'labels':labels,'data':data,'man':man}) 

def MAN_registration(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    return render(request,"MAN_registration.html",{'man':man}) 
    
def MAN_registrationstaff(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    return render(request,"MAN_registrationstaff.html",{'man':man}) 
     
def MAN_registrationstudent(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    return render(request,"MAN_registrationstudent.html",{'man':man}) 

def MAN_currentstaff(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    des = designation.objects.get(designation = "staff")
    mem = user_registration.objects.filter(status ="Active" or "active", designation_id = des)
    pay = payment.objects.all()
    return render(request,"MAN_currentstaff.html",{'mem':mem,'pay':pay,'man':man}) 

def MAN_resignedstaff(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    des = designation.objects.get(designation = "staff")
    mem = user_registration.objects.filter(status ="resign" or "Resigned", designation_id = des)
    pay = payment.objects.all()
    return render(request,"MAN_currentstaff.html",{'mem':mem,'pay':pay,'man':man})

def MAN_currentstudent(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    des = designation.objects.get(designation = "student")
    mem = user_registration.objects.filter(status ="Active" or "active", designation_id = des)
    pay = payment.objects.all()
    return render(request,"MAN_currentstudent.html",{'mem':mem,'pay':pay,'man':man}) 

def MAN_resignedstudent(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    des = designation.objects.get(designation = "student")
    mem = user_registration.objects.filter(status ="resign" or "Resigned", designation_id = des)
    pay = payment.objects.all()
    return render(request,"MAN_resignedstudent.html",{'mem':mem,'pay':pay,'man':man})

def MAN_academics(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        else:
            variable="dummy"
        man = user_registration.objects.filter(id=m_id) 
        return render(request,'MAN_academics.html',{'man':man})
    else:
        return redirect('/')

def MAN_batch(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    man = user_registration.objects.filter(id=m_id) 
    return render(request,"MAN_batch.html",{'man':man})

def MAN_addbatch(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
        variable="dummy"
    man = user_registration.objects.filter(id=m_id) 
    if request.method == "POST":
            m = batch()
            m.batch = request.POST['batch']
            m.description = request.POST['desc']
            m.save()
    return render(request,"MAN_addbatch.html",{'man':man})


def MAN_accsetting(request):
    if 'm_id' in request.session:
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        man = user_registration.objects.filter(id=m_id)
        return render(request,'MAN_accsetting.html', {'man': man})
    else:
        return redirect('/')



def MAN_accsettingimagechange(request,id):
    if 'm_id' in request.session:
        
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        man = user_registration.objects.filter(id=m_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('MAN_accsetting')
        return render(request, 'MAN_accsetting.html',{'man':man})
    else:
        return redirect('/')



def MAN_changepwd(request):
    if 'm_id' in request.session:
        
        if request.session.has_key('m_id'):
            m_id = request.session['m_id']
        
        man = user_registration.objects.filter(id=m_id)
    
        
        if request.method == 'POST':
            abc = user_registration.objects.get(id=m_id)
    
            oldps = request.POST['currentPassword']
            newps = request.POST['newPassword']
            cmps = request.POST.get('confirmPassword')
            if oldps != newps:
                if newps == cmps:
                    abc.password = request.POST.get('confirmPassword')
                    abc.save()
                    return render(request, 'MAN_profile.html', {'man': man})
    
            elif oldps == newps:
                messages.add_message(request, messages.INFO, 'Current and New password same')
            else:
                messages.info(request, 'Incorrect password same')
    
            return render(request,'MAN_changepwd.html')
    
        return render(request,'MAN_changepwd.html', {'man': man})
    
    else:
        return redirect('/')


#***************************paveen****************************
def Man_Academic_Subject(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    return render(request,'Man_Academic_Subject.html',{'man':man})


def Man_AddSubject(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    ba = batch.objects.all()
    return render(request,'Man_AddSubject.html',{'ba':ba,'man':man})

def Man_AddSubject_save(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    if request.method == 'POST':
        sub = request.POST['subject']       
        rate = request.POST['rate']
        ba = request.POST['batch']
        a=subject(subject=sub,batch_id=ba,Rate=rate)
        a.save()
        m="Subject added Successfully"
    return render(request,'Man_AddSubject.html',{'m':m,'man':man})
    

#*****************************subeesh***********************************
def Man_UpdateSubject(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    var= subject.objects.filter(id=id)
    vars=subject.objects.get(id=id)
    ba = batch.objects.all()
    return render(request,'Man_UpdateSubject.html',{'ba':ba,'vars':vars,'var':var,'man':man})

def Man_UpdateSubject_save(request,id):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    if request.method == 'POST':
        abc = subject.objects.get(id=id)
        abc.subject= request.POST.get('subject')
        abc.Rate = request.POST.get('rate')
        abc.batch_id = request.POST.get('batch')
        abc.save()
        m="Subject updated Successfully"
    return render(request,'Man_UpdateSubject.html',{'m':m,'man':man})

def Man_ViewSubject(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    man = user_registration.objects.filter(id=m_id)
    var =subject.objects.all()
    batch_id = request.GET.get('batch_id ')
    ba=batch.objects.filter(batch=batch_id)
    return render(request,'Man_ViewSubject.html',{'var':var,'ba':ba,'man':man})

def Man_deletesubject(request,id):
    m = subject.objects.get(id=id)
    m.delete()
    return redirect('Man_ViewSubject')


#*******************************anandhu**************************************
def MAN_AcademicClass(request):
       if request.session.has_key('m_id'):
            m_id = request.session['m_id']
       else:
            return redirect('/')     
       man = user_registration.objects.filter(id=m_id)
       return render(request, 'MAN_AcademicClass.html',{'man':man})

def MAN_AcademicAddClass(request):
       if request.session.has_key('m_id'):
           m_id = request.session['m_id']
       else:
            return redirect('/')    
       man = user_registration.objects.filter(id=m_id)
       Batc = batch.objects.all()
       return render(request, 'MAN_AcademicAddClass.html',{'man':man,'Batc':Batc})        


def MAN_AcademicAddClasssave(request):
    if request.session.has_key('m_id'):
        m_id = request.session['m_id']
    else:
            return redirect('/')
    man = user_registration.objects.filter(id=m_id)        
    if request.method == 'POST':
       newclass = request.POST['class']
       desc = request.POST['discrip']
       ba = request.POST['batch']
       a=class_registration(class_name=newclass,description=desc,batch_id=ba)
       a.save()
       m="Class added Successfully"
    return render(request,'MAN_AcademicAddClass.html',{'m':m,'man':man})

    #************************Super Admin module**************************



#************************Akhil***************************

def Admin_index(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)   
    return render(request,'Admin_index.html',{'Adm':Adm})

def Admin_dashboard(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)  
    return render(request,'Admin_dashboard.html',{'Adm':Adm})

def superadmin_logout(request):
    if 'SAdm_id' in request.session:  
        request.session.flush()
        return redirect("/")
    else:
        return redirect('/') 

def superadmin_changepwd(request):
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)  
        if request.method == 'POST':

            newPassword = request.POST.get('newPassword')
            confirmPassword = request.POST.get('confirmPassword')

            user = User.objects.get(is_superuser=True)
            if newPassword == confirmPassword:
                user.set_password(newPassword)
                user.save()
                msg_success = "Password has been changed successfully"
                return render(request, 'Admin_changepassword.html', {'msg_success': msg_success})
            else:
                msg_error = "Password does not match"
                return render(request, 'Admin_changepassword.html', {'msg_error': msg_error})
        return render(request,'Admin_changepassword.html',{'Adm':Adm})

#************************Nimisha**************************

#-------Academic---------
def Admin_Academic(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id) 
    return render(request,'Admin_Academic.html',{'Adm':Adm})

def Admin_Academic_Class(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id) 
    ba = batch.objects.all()
    return render(request,'Admin_Academic_Class.html',{'ba':ba,'Adm':Adm})

def Admin_AddClass(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id) 
    ba = batch.objects.all()
    return render(request,'Admin_AddClass.html',{'ba':ba,'Adm':Adm})


def Admin_ViewClass(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    var =class_registration.objects.all()
    batch_id = request.GET.get('batch_id ')
    ba=batch.objects.filter(batch=batch_id)
    return render(request,'Admin_ViewClass.html',{'var':var,'ba':ba,'Adm':Adm})

def Admin_add_classsave(request):
    
    if request.method == 'POST':
        newclass = request.POST['class']
        desc = request.POST['discrip']
        ba = request.POST['batch']
        a=class_registration(class_name=newclass,description=desc,batch_id=ba)
        a.save()
        m="Class added Successfully"
    return render(request,'Admin_AddClass.html',{'m':m})

def Admin_deleteclass(request,id):
    
    m = class_registration.objects.get(id=id)
    m.delete()
    return redirect('Admin_ViewClass')


def Admin_UpdateClass(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    var= class_registration.objects.filter(id=id)
    vars=class_registration.objects.get(id=id)
    ba = batch.objects.all()
    return render(request,'Admin_UpdateClass.html',{'ba':ba,'var':var,'vars':vars,'Adm':Adm})


def Admin_Update_Classsave(request,id):
    
    if request.method == 'POST':
        var = class_registration.objects.get(id=id)
        var.class_name= request.POST.get('class')
        var.description = request.POST.get('discrip')
        var.batch_name_id = request.POST.get('batch')
        var.save()
        m="Class updated Successfully"
    return render(request,'Admin_UpdateClass.html',{'m':m})

def Admin_Academic_Subject(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    return render(request,'Admin_Academic_Subject.html',{'Adm':Adm})

def Admin_AddSubject(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    ba = batch.objects.all()
    return render(request,'Admin_AddSubject.html',{'ba':ba,'Adm':Adm})

def Admin_AddSubject_save(request):
    
    if request.method == 'POST':
        sub = request.POST['subject']       
        rate = request.POST['rate']
        ba = request.POST['batch']
        a=subject(subject=sub,batch_id=ba,Rate=rate)
        a.save()
        m="Subject added Successfully"
    return render(request,'Admin_AddSubject.html',{'m':m})


def Admin_UpdateSubject(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    var= subject.objects.filter(id=id)
    vars=subject.objects.get(id=id)
    ba = batch.objects.all()
    return render(request,'Admin_UpdateSubject.html',{'ba':ba,'vars':vars,'var':var,'Adm':Adm})

def Admin_UpdateSubject_save(request,id):
    
    if request.method == 'POST':
        abc = subject.objects.get(id=id)
        abc.subject= request.POST.get('subject')
        abc.Rate = request.POST.get('rate')
        abc.batch_id = request.POST.get('batch')
        abc.save()
        m="Subject updated Successfully"
    return render(request,'Admin_UpdateSubject.html',{'m':m})

def Admin_ViewSubject(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    var = subject.objects.all()
    batch_id = request.GET.get('batch_id ')
    ba=batch.objects.filter(batch=batch_id)
    return render(request,'Admin_ViewSubject.html',{'var':var,'ba':ba,'Adm':Adm})

def Admin_deletesubject(request,id):
    
    m = subject.objects.get(id=id)
    m.delete()
    return redirect('Admin_ViewSubject')

#------Attendance--------

def Admin_Attendance(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    b1=batch.objects.all()
    u1=user_registration.objects.all()
    return render(request,'Admin_Attendance.html',{'b1':b1,'u1':u1,'Adm':Adm})

def Admin_Attendance_Show(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    if request.method == "POST":
        empname1=request.POST.get('empname')      
        atten=attendance.objects.filter(user_id=empname1).order_by("-id")
    return render(request,'Admin_AttendanceShow.html',{'atten':atten,'empname':empname1,'Adm':Adm})


def Admin_At_Designation(request): 
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    dept_id = request.GET.get('dept_id') 
    Desig = designation.objects.all()
    # Desig = designation.objects.all()
    print(Desig)
    return render(request, 'Admin_At_Designation.html', {'Desig': Desig,'Adm':Adm})
    
def Admin_At_Name(request):   
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    emp = user_registration.objects.filter(designation_id=desig_id).filter(batch_id=dept_id)
    print(emp)
    return render(request, 'Admin_At_Name.html', {'emp': emp,'Adm':Adm})

#----------Reported issue------

def Admin_Reportedissues_Card(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    Desig = designation.objects.all()
    return render(request,'Admin_Reportedissues_Card.html',{'designation':Desig,'Adm':Adm})

def Admin_Reportedissues(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    reported_issues=reported_issue.objects.get(id=id)
    user_reg=user_registration.objects.all()
    return render(request,'Admin_Reportedissues.html',{'reported_issue':reported_issues,'user':user_reg,'Adm':Adm})
   

def Admin_Reportedissuetomanager(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    des=designation.objects.get(designation="manager")
    # user_reg=user_registration.objects.filter(id=SAdm_id)
    var=reported_issue.objects.filter(reporter_id=des.id).order_by("-id")
    return render(request,'Admin_Reportedissuetomanager.html',{'var':var,'Adm':Adm})


def Adminreplyview(request,id):
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        reported_issues=reported_issue.objects.filter(id=id)
        return render(request,'Adminreplyview.html',{'reported_issue':reported_issues,'Adm':Adm})

def Adminissuereply(request,id):
    
        if request.method == 'POST':
            v = reported_issue.objects.get(id=id)
            v.reply=request.POST.get('reply')
            v.save()
        return redirect('Admin_Reportedissues_Card')


def Admin_Reportedissues_Show(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    reported_issues=reported_issue.objects.all()
    designations=designation.objects.get(id=id)
    user=user_registration.objects.filter(designation=designations).order_by("-id")
    return render(request,'Admin_Reportedissues_Show.html',{'designation':designations,'Adm':Adm,'reported_issue':reported_issues,'user_registration':user})

#---------Leave-------

def Admin_LeaveRequest(request):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        return redirect('/')
    Adm = user_registration.objects.filter(id=SAdm_id)
    Man = designation.objects.get(designation='manager')
    var = Leave.objects.filter(designation_id=Man.id).all().order_by("-id")
    return render(request,'Admin_LeaveRequest.html',{'var':var,'Adm':Adm})


def Admin_rejectedManager_leave(request,id):
    
    if request.method == 'POST':
        staff_reason=request.POST.get('reply')
        pro_sts = Leave.objects.filter(id=id).update(leave_rejected_reason= staff_reason,leaveapprovedstatus ='Rejected')      
        return redirect('Admin_LeaveRequest')

def Admin_acceptedManager_leave(request,id):
    if request.session.has_key('SAdm_id'):
        SAdm_id = request.session['SAdm_id']
    else:
        variable="dummy"    
    al = Leave.objects.filter(id=id).update(leaveapprovedstatus ='Approved')     
    return redirect('Admin_ManagerLeaveRequest')


#***************************************Anandhu********************************

def Registration_Admin(request):
    # if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        Desig = designation.objects.all()
        Student = designation.objects.filter(designation = 'student')
        Staff = designation.objects.filter(designation = 'staff')
        return render(request, 'Registration_Admin.html',{'Desig':Desig,'Student':Student,'Staff':Staff,'Adm':Adm})    

def RegistrationStaff_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        id=id
        return render(request, 'RegistrationStaff_Admin.html',{'Adm':Adm})      

def RegistrationStudent_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        id=id    
        return render(request,'RegistrationStudent_Admin.html',{'Adm':Adm})       

def RegistrationCurrentStaff_Admin(request):
    #    f 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='staff')
        CStaff = user_registration.objects.filter(designation_id = des).filter(status='active' or 'Active').all().order_by('-id')
        batc = batch.objects.all()
        class_reg = class_registration.objects.all()
        paymen = payment.objects.all()
        return render(request, 'RegistrationCurrentStaff_Admin.html',{'Adm':Adm,'des':des,'CStaff':CStaff,'batc':batc,'class_reg':class_reg,'payment':paymen})  

def RegistrationCurrentStaff_Adminsave(request,id):
    
   
    if request.method == 'POST':
       a = user_registration.objects.get(id=id)
   
       a.status = request.POST['status']
       BatchId = request.POST['batch'] 
       a.batch_id = BatchId 
       ClassId = request.POST['class'] 
       a.class_registration_id = ClassId
       a.save()
     
       return redirect('RegistrationCurrentStaff_Admin')


def RegistrationCurrentStaffAdmin_update(request,id):
    # if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        
        mem1 = user_registration.objects.get(id=id)
        pay = payment.objects.filter(user_id=id)
        bac = batch.objects.all()
        clss = class_registration.objects.all()
        
        return render(request,'RegistrationCurrentStaffAdmin_update.html',{'Adm':Adm,'pay':pay,'mem1':mem1,'clss':clss,'bac':bac})
 


def RegistrationCurrentStaffAdmin_updatessave(request,id):
    
    a = user_registration.objects.get(id=id)
    b = payment.objects.get(user_id=id)
    if request.method == 'POST':
       a.fullname = request.POST.get('name')
       a.email = request.POST.get('email')
       a.mobile = request.POST.get('mobile')
       a.status = request.POST.get('status')
       a.dateofappointment  =  request.POST.get('dateofappo')
       a.staff_id =  request.POST.get('employeeid')
       BatchId = request.POST.get('batch')
       a.batch_id = BatchId 
       ClassId = request.POST.get('class')
       a.class_registration_id = ClassId
       a.save()
                    

    return redirect('RegistrationCurrentStaff_Admin')


def RegistrationCurrentStaffAdmin_delete(request,id):
    
    m =   user_registration.objects.get(id = id)
    m.delete()
    return redirect('RegistrationCurrentStaff_Admin')

def RegistrationResignedStaff_Admin(request):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        des1 = designation.objects.get(designation='staff')
        RStaff = user_registration.objects.filter(designation_id = des1).filter(status='resign' or 'resigned' or 'Resigned').all().order_by('-id')
        batc1 = batch.objects.all()
        class_reg1 = class_registration.objects.all()
        payment1 = payment.objects.all()
        return render(request, 'RegistrationResignedStaff_Admin.html',{'Adm':Adm,'des1':des1,'RStaff':RStaff,'batc1':batc1,'class_reg1':class_reg1,'payment1':payment1})  


def RegistrationResignedStaffAdmin_update(request,id):
    # if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        
        mem1 = user_registration.objects.get(id=id)
        pay = payment.objects.filter(user_id=id)
        bac = batch.objects.all()
        clss = class_registration.objects.all()
        
        return render(request,'RegistrationResignedStaffAdmin_update.html',{'Adm':Adm,'pay':pay,'mem1':mem1,'clss':clss,'bac':bac})
    




def RegistrationResignedStaffAdmin_updatessave(request,id):
        
    a = user_registration.objects.get(id=id)
    if request.method == 'POST':
       a.fullname = request.POST['name']
       a.email = request.POST['email']
       a.mobile = request.POST['mobile']
       a.status = request.POST['status'] 
       BatchId = request.POST['batch'] 
       a.batch_id = BatchId 
       ClassId = request.POST['class'] 
       a.class_registration_id = ClassId
       a.save()
              

    return redirect('RegistrationResignedStaff_Admin')


def RegistrationResignedStaffAdmin_delete(request,id):
    
    
    m =   user_registration.objects.get(id = id)
    m.delete()
    return redirect('RegistrationResignedStaff_Admin')


def RegistrationCurrentStudent_Admin(request):
        # if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='student')
        CStudent = user_registration.objects.filter(designation_id = des).filter(status='active' or 'Active').all().order_by('-id')
        batc2 = batch.objects.all()
        class_reg2 = class_registration.objects.all()
        paymen = payment.objects.all()
        return render(request, 'RegistrationCurrentStudent_Admin.html',{'Adm':Adm,'payment':paymen,'des':des,'CStudent':CStudent,'batc2':batc2,'class_reg2':class_reg2})     

def RegistrationCurrentStudent_Adminsave(request,id):
    
   
    if request.method == 'POST':
       a = user_registration.objects.get(id=id)
   
       BatchId = request.POST['batch'] 
       a.batch_id = BatchId 
       ClassId = request.POST['class'] 
       a.class_registration_id = ClassId
       a.save()
     
       return redirect('RegistrationCurrentStudent_Admin')


def RegistrationPreviousstudent_Admin(request):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='student')
        PStudent = user_registration.objects.filter(designation_id = des).filter(status='resign' or 'resigned').all().order_by('-id')
        batc3 = batch.objects.all()
        class_reg3 = class_registration.objects.all()
        paymen = payment.objects.all()
        return render(request, 'RegistrationPreviousstudent_Admin.html',{'Adm':Adm,'payment':paymen,'des':des,'PStudent':PStudent,'batc3':batc3,'class_reg3':class_reg3})                              


def RegistrationCurrentStudentAdmin_update(request,id):
    # if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        
        mem1 = user_registration.objects.get(id=id)
        pay = payment.objects.filter(user_id=id)
        bac = batch.objects.all()
        clss = class_registration.objects.all()
        
        return render(request,'RegistrationCurrentStudentAdmin_update.html',{'Adm':Adm,'pay':pay,'mem1':mem1,'clss':clss,'bac':bac})
    # else:
    #     return redirect('/')

def RegistrationCurrentStudent_updatessave(request,id):
    # if 'SAdm_id' in request.session:
    #     if request.session.has_key('SAdm_id'):
    #         SAdm_id = request.session['SAdm_id']
    #     else:
    #         return redirect('/') 
    #     SAdm = user_registration.objects.filter(id=SAdm_id) 
    a = user_registration.objects.get(id=id)
    # b = payment.objects.get(user_id=id)
    if request.method == 'POST':
       a.fullname = request.POST.get('name')
       a.email = request.POST.get('email')
       a.mobile = request.POST.get('mobile')
       a.status = request.POST.get('status')
       a.student_id  =  request.POST.get('studentid')
       a.joiningdate =  request.POST.get('joiningdate')
       BatchId = request.POST.get('batch') 
       a.batch_id = BatchId 
       ClassId = request.POST.get('class') 
       a.class_registration_id = ClassId
       a.save()
              

    return redirect('RegistrationCurrentStudent_Admin')


def RegistrationCurrentStudentAdmin_delete(request,id):
    
    
    m =   user_registration.objects.get(id = id)
    m.delete()
    return redirect('RegistrationCurrentStudent_Admin')


def RegistrationPreviousstudentAdmin_update(request,id):
    # if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        
        mem1 = user_registration.objects.get(id=id)
        pay = payment.objects.filter(user_id=id)
        bac = batch.objects.all()
        clss = class_registration.objects.all()
        
        return render(request,'RegistrationPreviousstudentAdmin_update.html',{'Adm':Adm,'pay':pay,'mem1':mem1,'clss':clss,'bac':bac})
    # else:
    #     return redirect('/')


def RegistrationPreviousstudentAdmin_updatessave(request,id):
    # if 'SAdm_id' in request.session:
    #     if request.session.has_key('SAdm_id'):
    #         SAdm_id = request.session['SAdm_id']
    #     else:
    #         return redirect('/') 
    #     SAdm = user_registration.objects.filter(id=SAdm_id) 
    a = user_registration.objects.get(id=id)
    # b = payment.objects.get(user_id=id)
    if request.method == 'POST':
       a.fullname = request.POST.get('name')
       a.email = request.POST.get('email')
       a.mobile = request.POST.get('mobile')
       a.joiningdate = request.POST.get('joiningdate')
       a.status = request.POST.get('status')
       a.student_id  =  request.POST.get('studentid')
       BatchId = request.POST.get('batch')
       a.batch_id = BatchId 
       ClassId = request.POST.get('class')
       a.class_registration_id = ClassId
       a.save()
            
    return redirect('RegistrationPreviousstudent_Admin')


def RegistrationPreviousstudentAdmin_delete(request,id):
    
    
    m =   user_registration.objects.get(id = id)
    m.delete()
    return redirect('RegistrationPreviousstudent_Admin')

def Staff_Admin(request):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        return render(request, 'Staff_Admin.html',{'Adm':Adm}) 

def StaffCurrentstaff_Admin(request):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='staff')
        SCurrentstaff = user_registration.objects.filter(designation_id = des).filter(status='active' or 'Active').all().order_by('-id')
        return render(request, 'StaffCurrentstaff_Admin.html',{'Adm':Adm,'des':des,'SCurrentstaff':SCurrentstaff}) 

def StaffPreviousstaff_Admin(request):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='staff')
        PCurrentstaff = user_registration.objects.filter(designation_id = des).filter(status='resign' or 'Resgined').all().order_by('-id')
        return render(request, 'StaffPreviousstaff_Admin.html',{'Adm':Adm,'des':des,'PCurrentstaff':PCurrentstaff}) 

def StaffCurrentstaffProfile_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        CStaffProfile = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'StaffCurrentstaffProfile_Admin.html',{'labels':labels,'data':data,'Adm':Adm,'CStaffProfile':CStaffProfile}) 

def StaffPreviousstaffProfile_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
       
        PStaffProfile = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'StaffPreviousstaffProfile_Admin.html',{'labels':labels,'data':data,'Adm':Adm,'PStaffProfile':PStaffProfile}) 

def StaffPreviousstaffPerformance_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       Adm = user_registration.objects.filter(id=SAdm_id)
       var = user_registration.objects.get(id=id)
       return render(request,'StaffPreviousstaffPerformance_Admin.html',{'Adm':Adm,'var':var})

def StaffPreviousstaffPerformance_Adminsave(request,id):
     if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
     else:
            return redirect('/')          
     Adm = user_registration.objects.filter(id=SAdm_id)           
     if request.method == "POST":
            var = user_registration.objects.get(id=id)
            var.creativity = request.POST.get('create')
            var.workperformance = request.POST.get('work')
            var.attitude = request.POST.get('attitu')
            var.save()
            m2 ="Datas added Successfully"
            return render(request,'StaffPreviousstaffPerformance_Admin.html',{'m2':m2,'Adm':Adm,'var':var})

def StaffCurrentstaffAttendance_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        id = id
        return render(request, 'StaffCurrentstaffAttendance_Admin.html',{'Adm':Adm,'id':id})  

def StaffCurrentstaffAttendanceSort_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        id=id
        if request.method == "POST":
            fromdate = request.POST.get('from')
            todate = request.POST.get('to') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request,'StaffCurrentstaffAttendanceSort_Admin.html',{'Adm':Adm,'mem1':mem1,'id':id})            

def StaffCurrentstaffPerformance_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       Adm = user_registration.objects.filter(id=SAdm_id)
       var = user_registration.objects.get(id=id)
       return render(request,'StaffCurrentstaffPerformance_Admin.html',{'Adm':Adm,'var':var})


def StaffCurrentstaffPerformance_Adminsave(request,id):
     if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
     else:
            return redirect('/')          
     Adm = user_registration.objects.filter(id=SAdm_id)           
     if request.method == "POST":
            var = user_registration.objects.get(id=id)
            var.creativity = request.POST.get('create')
            var.workperformance = request.POST.get('work')
            var.attitude = request.POST.get('attitu')
            var.save()
            m1 ="Datas added Successfully"
            return render(request,'StaffCurrentstaffPerformance_Admin.html',{'m1':m1,'Adm':Adm,'var':var})

def StaffPreviousstaffAttendance_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        id = id
        return render(request, 'StaffPreviousstaffAttendance_Admin.html',{'Adm':Adm,'id':id})  

def StaffPreviousstaffAttendanceSort_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        id=id
        if request.method == "POST":
            fromdate = request.POST.get('from')
            todate = request.POST.get('to') 
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request,'StaffPreviousstaffAttendanceSort_Admin.html',{'Adm':Adm,'mem1':mem1,'id':id})


def Student_Admin(request):
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        return render(request, 'Student_Admin.html',{'Adm':Adm}) 

def StudentCurrentstudent_Admin(request):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='student')
        SCurrentstudent = user_registration.objects.filter(designation_id = des).filter(status='active' or 'Active')
        return render(request, 'StudentCurrentstudent_Admin.html',{'Adm':Adm,'des':des,'SCurrentstudent':SCurrentstudent}) 


def StudentPreviousstudent_Admin(request):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        des = designation.objects.get(designation='student')
        PCurrentstudent = user_registration.objects.filter(designation_id = des).filter(status='resign' or 'resigned')
        return render(request, 'StudentPreviousstudent_Admin.html',{'Adm':Adm,'des':des,'PCurrentstudent':PCurrentstudent}) 

def StudentCurrentstudentProfile_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        CStudentProfile = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'StudentCurrentstudentProfile_Admin.html',{'labels':labels,'data':data,'Adm':Adm,'CStudentProfile':CStudentProfile})

def StudentPreviousstudentProfile_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        PStudentProfile = user_registration.objects.get(id = id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request, 'StudentPreviousstudentProfile_Admin.html',{'labels':labels,'data':data,'Adm':Adm,'PStudentProfile':PStudentProfile})

def StudentCurrentstudentPerformance_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       Adm = user_registration.objects.filter(id=SAdm_id)
       var = user_registration.objects.get(id=id)
       return render(request,'StudentCurrentstudentPerformance_Admin.html',{'Adm':Adm,'var':var})

def StudentPreviousstudentPerformance_Admin(request,id):
       if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
       else:
            return redirect('/')
       mem = user_registration.objects.filter(id=SAdm_id)
       var = user_registration.objects.get(id=id)
       return render(request,'StudentPreviousstudentPerformance_Admin.html',{'mem':mem,'var':var})


def StudentPreviousstudentPerformance_Adminsave(request,id):
     if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
     else:
            return redirect('/')          
     mem = user_registration.objects.filter(id=SAdm_id)           
     if request.method == "POST":
            var = user_registration.objects.get(id=id)
            var.creativity = request.POST.get('create')
            var.workperformance = request.POST.get('work')
            var.attitude = request.POST.get('attitu')
            var.save()
            m4 ="Datas added Successfully"
            return render(request,'StudentPreviousstudentPerformance_Admin.html',{'m4':m4,'mem':mem,'var':var})

def StudentCurrentstudentPerformance_Adminsave(request,id):
     if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
     else:
            return redirect('/')          
     Adm = user_registration.objects.filter(id=SAdm_id)           
     if request.method == "POST":
            var = user_registration.objects.get(id=id)
            var.creativity = request.POST.get('create')
            var.workperformance = request.POST.get('work')
            var.attitude = request.POST.get('attitu')
            var.save()
            m3 ="Datas added Successfully"
            return render(request,'StudentCurrentstudentPerformance_Admin.html',{'m3':m3,'Adm':Adm,'var':var})

def StudentCurrentstudentAttendance_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        id = id
        return render(request, 'StudentCurrentstudentAttendance_Admin.html',{'Adm':Adm,'id':id}) 

def StudentCurrentstudentAttendanceSort_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        id=id
        if request.method == "POST":
                fromdate = request.POST.get('from')
                todate = request.POST.get('to') 
                mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request,'StudentCurrentstudentAttendanceSort_Admin.html',{'Adm':Adm,'mem1':mem1,'id':id})

def StudentPreviousstudentAttendance_Admin(request,id):
    #    if 'SAdm_id' in request.session:
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        id = id
        return render(request, 'StudentPreviousstudentAttendance_Admin.html',{'Adm':Adm,'id':id})
      
def StudentPreviousstudentAttendanceSort_Admin(request,id):
    #    if 'SAdm_id' in request.session:
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        id=id
        if request.method == "POST":
                fromdate = request.POST.get('from')
                todate = request.POST.get('to') 
                mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id = id)
        return render(request,'StudentPreviousstudentAttendanceSort_Admin.html',{'Adm':Adm,'mem1':mem1,'id':id})        



def Academic_Admin(request):
        if 'SAdm_id' in request.session:
            if request.session.has_key('SAdm_id'):
             SAdm_id = request.session['SAdm_id']
            else:
                return redirect('/')
            Adm = user_registration.objects.filter(id=SAdm_id)
            return render(request, 'Academic_Admin.html',{'Adm':Adm}) 

def AcademicBatch_Admin(request):
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        return render(request,'AcademicBatch_Admin.html',{'Adm':Adm})

def AcademicAddBatch_Admin(request):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        Batc = batch.objects.all()
        return render(request, 'AcademicAddBatch_Admin.html',{'Batc':Batc,'Adm':Adm}) 


def AcademicAddBatch_Adminsave(request):
    #    if 'SAdm_id' in request.session:
    #         if request.session.has_key('SAdm_id'):
    #          SAdm_id = request.session['SAdm_id']
    #    else:
    #         return redirect('/')
    #    mem = user_registration.objects.filter(id=SAdm_id)
       if request.method == 'POST':
            desc = request.POST['discrip']
            ba = request.POST['batch']
            a=batch(description=desc,batch=ba)
            a.save()
            m="Batch added Successfully"
       return render(request, 'AcademicAddBatch_Admin.html',{'m':m}) 

def AcademicAddBatchUpdate_Admin(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        var= batch.objects.filter(id=id)
        var1= batch.objects.get(id=id)
        batc = batch.objects.all()
        return render(request, 'AcademicAddBatchUpdate_Admin.html',{'Adm':Adm,'batc':batc,'var':var,'var1':var1}) 

def AcademicAddBatchUpdate_Adminsave(request,id):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)
        if request.method == 'POST':
                a=batch.objects.get(id=id)
                a.desc = request.POST.get('discrip')
                a.batch = request.POST.get('batch')
                a.save()
                m="Batch updated Successfully"
        return render(request,'AcademicAddBatch_Admin.html',{'m':m,'Adm':Adm})


def AcademicViewBatch_Admin(request):
    #    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        Adm = user_registration.objects.filter(id=SAdm_id)

        batc = batch.objects.all()
        clss = class_registration.objects.all()
        return render(request, 'AcademicViewBatch_Admin.html',{'Adm':Adm,'batc':batc,'clss':clss})

def AcademicAddBatch_Admindelete(request,id):
       
       m =batch.objects.get(id = id)
       m.delete()
       return redirect('AcademicBatch_Admin')  


#***********************Account module***************************

#*************************Subeesh*******************************

def Acc_index(request):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        
        return render(request,'Acc_index.html')

def account_dashboard(request):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        
        acc = user_registration.objects.filter(id=acc_id)
        labels = []
        data = []
        queryset = user_registration.objects.filter(id=acc_id)
        for i in queryset:
            labels=[i.workperformance,i.attitude,i.creativity]
            
            
            data=[i.workperformance,i.attitude,i.creativity]
        return render(request,'account_dashboard.html',{'labels':labels,'data':data,'acc':acc})

def Account_Student_det(request):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        
        acc = user_registration.objects.filter(id=acc_id)
        return render(request, 'Account_Student_det.html',{'acc':acc})

def Account_previous_students(request):
    des = designation.objects.get(designation='student')
    aps = user_registration.objects.filter(status ="resign" or "Resigned", designation_id = des)
    pay = payment.objects.all()
    return render(request, 'Account_previous_students.html',{'aps': aps,'pay':pay})

def account_accsetting(request):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        
        acc = user_registration.objects.filter(id=acc_id)
        return render(request,'account_accsetting.html', {'acc': acc})
    else:
        return redirect('/')

def account_accsettingimagechange(request,id):
    if 'acc_id' in request.session:
        
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        
        acc = user_registration.objects.filter(id=acc_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('account_accsetting')
        return render(request, 'account_accsetting.html',{'acc':acc})
    else:
        return redirect('/')

def Acc_current_students(request):
     if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
                acc_id = request.session['acc_id']
        else:
            variable = "dummy"
        acc = user_registration.objects.filter(id=acc_id)
       
        des = designation.objects.get(designation='student')
        acs = user_registration.objects.filter(designation_id=des).filter(status='active') .all().order_by('-id')
        time = datetime.now()
        pay = payment.objects.all().order_by('-id')
     return render(request, 'Acc_current_students.html',{'acc':acc,'acs':acs,'time':time,'pay':pay})


def Acc_current_students_payment(request,id):
     if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
                acc_id = request.session['acc_id']
        else:
            variable = "dummy"
        acc = user_registration.objects.filter(id=acc_id)
        
        if request.method == 'POST':
            payuser=user_registration.objects.get(id=id)
            pay=payment()
            pay.date = datetime.now()
            pay.payment = request.POST['p']
            pay.user = payuser
            pay.save()
            return redirect('Acc_current_students')
        return render(request,"Acc_current_students.html",{'acc':acc})


#************************Sharon****************************************

def account_leaverequest(request):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"
        acc = user_registration.objects.filter(id=acc_id)
    return render(request,"account_leaverequest.html",{'acc':acc})

def account_applyleave(request):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"
        acc = user_registration.objects.filter(id=acc_id)
        # pro = user_registration.objects.filter(designation_id=usernameacnt)
        des=designation.objects.get(designation="account")
        if request.method == "POST":
            m1 = Leave()
            m1.from_date = request.POST.get('from')
            m1.to_date = request.POST.get('to')
            m1.leave_status = request.POST.get('haful')
            m1.reason = request.POST.get('reason')
            m1.designation_id = des.id
            m1.user_id = acc_id
            m1.status = "pending"
            m1.save()
        return render(request, 'account_applyleave.html',{'acc':acc})  
    else:
        return redirect('/')
        
def account_requestedleave(request):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"
        acc = user_registration.objects.filter(id=acc_id)
        var = Leave.objects.filter(user_id=acc_id).order_by("-id")
        return render(request, 'account_requestedleave.html',{'acc':acc,'var':var}) 
    else:
        return redirect('/')

def account_issues(request):
    if request.session.has_key('acc_id'):
        acc_id = request.session['acc_id']
    else:
        return redirect('/')
    acc = user_registration.objects.filter(id=acc_id)
    return render(request,"account_issues.html",{'acc':acc})

def account_reportedissue(request):
    if request.session.has_key('acc_id'):
        acc_id = request.session['acc_id']
    else:
        return redirect('/')
    acc = user_registration.objects.filter(id=acc_id)
    var = reported_issue.objects.filter(reporter=acc_id)
    return render(request,"account_reportedissue.html",{'var':var,'acc':acc})

    
def account_issuereply(request,id):
    if request.session.has_key('acc_id'):
        acc_id = request.session['acc_id']
    else:
        return redirect('/')
    acc = user_registration.objects.filter(id=acc_id)
    rid=request.GET.get('rid')
    var=reported_issue.objects.filter(id=id)
    
    return render(request, 'account_issuereply.html',{'var':var,'acc':acc})
    


def account_report_an_issue(request):
    if request.session.has_key('acc_id'):
        acc_id = request.session['acc_id']
    else:
        return redirect('/')
    acc = user_registration.objects.filter(id=acc_id)
    design=designation.objects.get(designation="manager")
    man = user_registration.objects.get(designation_id=design.id)
    if request.method == 'POST':
        vars = reported_issue()
        vars.issue=request.POST.get('report')
        vars.reported_date=datetime.now()
        vars.reported_to_id=man.id
        vars.reporter_id=acc_id
        vars.status='pending'
        vars.save()
    return render(request,"account_report_an_issue.html",{'acc':acc})
   

def account_changepassword(request):
    
    if 'acc_id' in request.session:
        
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']     
        acc = user_registration.objects.filter(id=acc_id)   
          
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            cur = abc.password
            oldps = request.POST["currentPassword"]
            newps = request.POST["newPassword"]
            cmps = request.POST["confirmPassword"]
            if oldps == cur:
                if oldps != newps:
                    if newps == cmps:
                        abc.password = request.POST.get('confirmPassword')
                        abc.save()
                        return render(request, 'account_changepassword.html', {'acc': acc})
                elif oldps == newps:
                    messages.add_message(request, messages.INFO, 'Current and New password same')
                else:
                    messages.info(request, 'Incorrect password same')

                return render(request, 'account_changepassword.html', {'acc': acc})
            else:
                messages.add_message(request, messages.INFO, 'old password wrong')
                return render(request, 'account_changepassword.html', {'acc': acc})
        return render(request, 'account_changepassword.html', {'acc': acc})
                 
    else:
        return redirect('/')


def account_logout(request):
    if 'acc_id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')


def Accounts_Staff(request):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"  
        acc= user_registration.objects.filter(id=acc_id)  
        return render(request,'Accounts_Staff.html',{'acc':acc})
    else:
        return redirect('/') 
    
def Accounts_CurrentStaff(request):  
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"  
        acc = user_registration.objects.filter(id=acc_id)  
        stud_data = designation.objects.get(designation='staff')
        studname =user_registration.objects.filter(status='active').filter(designation=stud_data)
        return render(request,'Accounts_CurrentStaff.html',{'var':studname,'acc':acc})
    else:
        return redirect('/') 

def Accounts_CurrentStaffAddaccount(request,id): 
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"  
        acc = user_registration.objects.filter(id=acc_id)  
        var=user_registration.objects.filter(id=id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.bank_name= request.POST.get('bankname')
            abc.bank_branch = request.POST.get('branchname')
            abc.account_no = request.POST.get('number')
            abc.ifsc = request.POST.get('ifsccode')
            abc.save()
        return render(request,'Accounts_CurrentStaffAddaccount.html',{'var':var,'acc':acc})
    else:
        return redirect('/') 
    
def Accounts_CurrentStaffpayslip(request):  
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"  
        acc = user_registration.objects.filter(id=acc_id)  
        b1 = batch.objects.all()
        des = designation.objects.all()    
        return render(request,'accounts_payslip.html',{'b1':b1,'des':des,'acc':acc})
    else:
        return redirect('/') 


@csrf_exempt
def accounts_acntpay(request):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"  
        acc = user_registration.objects.filter(id=acc_id)  
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        dept_id = int(request.POST['depmt'])
        desig_id = int(request.POST['desi'])  
        names = acntspayslip.objects.filter(fromdate_range=(fdate,tdate),designation_id= desig_id, batch_id= dept_id).values('user_idfullname','eno', 'user_idaccount_no', 'user_idbank_name', 'user_idbank_branch','user_idid', 'user_id_email','id').order_by("-id")
        print(fdate)
        print(tdate)
        print(dept_id)
        print(desig_id)
        print(names)
        return render(request,'accounts_acntpay.html', {'names':names,'acc':acc})
    else:
        return redirect('/') 

def accounts_paydetails(request,id,tid):  
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"  
        acc = user_registration.objects.filter(id=acc_id)   
        user = user_registration.objects.get(id=tid)
        acc1 = acntspayslip.objects.get(id=id)
        names = acntspayslip.objects.all()
        return render(request,'accounts_paydetails.html', {'acc':acc, 'user':user,'acc1':acc1})
    else:
        return redirect('/') 


def accounts_print(request,id,tid):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"  
        acc = user_registration.objects.filter(id=acc_id)
        user = user_registration.objects.get(id=tid)
        acc1 = acntspayslip.objects.get(id=id)
        return render(request,'accounts_print.html', {'acc':acc, 'user':user,'acc1':acc1})
    else:
        return redirect('/') 

def account_payment_details(request,id):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"  
        acc = user_registration.objects.filter(id=acc_id) 
        vars=user_registration.objects.get(id=id)
        context = {'vars':vars,'acc':acc}
        return render(request,'account_payment_details.html', context)
    else:
        return redirect('/')     

def account_payment_salary(request,id):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"  
        acc = user_registration.objects.filter(id=acc_id) 
        vars=user_registration.objects.get(id=id)
        if request.method == "POST":
            abc = acntspayslip()
            abc.basic_salary = request.POST["salary"]
            abc.hra = request.POST["hra"]
            abc.conveyns = request.POST["ca"]
            abc.pf_tax = request.POST["pt"]
            abc.incentives = request.POST["ins"]
            abc.delay = request.POST["delay"]
            abc.leavesno= request.POST["leave"]
            abc.fromdate= request.POST["efdate"]
            abc.tax = 0
            abc.pf = request.POST["pf"]
            abc.incometax = 0
            abc.basictype = request.POST["basictype"]
            abc.pftype = request.POST["pftype"]
            abc.esitype = request.POST["esitype"]
            abc.hratype = request.POST["hratype"]
            abc.contype = request.POST["contype"]
            abc.protype = request.POST["protype"]
            abc.instype = request.POST["instype"]
            abc.deltype = request.POST["deltype"]
            abc.leatype = request.POST["leatype"]
            abc.esi = request.POST["esi"] 
            abc.user_id_id = vars.id
            abc.batch_id = vars.batch.id
            abc.designation_id = vars.designation.id
            abc.save()
        return render(request, 'account_payment_salary.html',{'vars':vars,'acc':acc})
    else:
        return redirect('/')     
   
def account_payment_view(request,id):
    if 'acc_id' in request.session:
        if request.session.has_key('acc_id'):
            acc_id = request.session['acc_id']
        else:
            variable="dummy"  
        acc = user_registration.objects.filter(id=acc_id) 
        reg =user_registration.objects.get(id=id)
        use=acntspayslip.objects.filter(user_id_id=id)
        return render(request,'account_payment_view.html',{'reg':reg,'use':use,'acc':acc})
    else:
        return redirect('/')



def Account_staffprevious(request):
    if request.session.has_key('acc_id'):
        acc_id = request.session['acc_id']
    else:
        return redirect('/')
    acc = user_registration.objects.filter(id=acc_id)
    staff=designation.objects.get(designation='Staff')
    user=user_registration.objects.filter(designation=staff)
    pay=acntspayslip.objects.all()
    return render(request,'Account_staffprevious.html',{'user_registration':user,'paymentlist':pay,'acc':acc})