import os
import random
from django.shortcuts import render, redirect
from app.models import *
from datetime import datetime,date
from django.http import HttpResponse, HttpResponseRedirect
from django. contrib import messages
from django.conf import settings
from django.http import HttpResponse


def login(request):
    
    staff = designation.objects.get(designation="staff")
    
    if request.method == 'POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation=staff.id,status="active").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['st_id'] = member.designation_id
                request.session['usernamets1'] = member.fullname
                request.session['st_id'] = member.id 
                mem=user_registration.objects.filter(id= member.id)
                
                return render(request,'Staff_dashboard.html',{'mem':mem})
    
        else:
                context = {'msg_error': 'Invalid data'}
                return render(request, 'login.html', context)

       
    return render(request,'login.html')


def Staff_logout(request):
    if 'id' in request.session:  
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def Staff_index(request):
    if 'st_id' in request.session:
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=st_id)
        return render(request,'Staff_index.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_accsetting(request):
    if 'st_id' in request.session:
        
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=st_id)
        return render(request,'Staff_accsetting.html', {'mem': mem})
    else:
        return redirect('/')

def Staff_accsettingimagechange(request,id):
    if 'st_id' in request.session:
        
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=st_id)
        if request.method == 'POST':
            abc = user_registration.objects.get(id=id)
            abc.photo = request.FILES['filename']
            abc.save()
            return redirect('Staff_accsetting')
        return render(request, 'Staff_accsetting.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_changepwd(request):
    
    if 'st_id' in request.session:
        
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']     
        mem = user_registration.objects.filter(id=st_id)   
          
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
    if 'st_id' in request.session:
        
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=st_id)
        return render(request,'Staff_dashboard.html', {'mem': mem})
    else:
        return redirect('/')

def Staff_attendance(request):
    if 'st_id' in request.session:
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=st_id)
        return render(request, 'Staff_attendance.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_attendancesort(request):
    if 'st_id' in request.session:
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=st_id)
        if request.method == "POST":
            fromdate = request.POST.get('fromdate')
            todate = request.POST.get('todate') 
            # mem1 = attendance.objects.raw('select * from app_attendance where user_id and date between "'+fromdate+'" and "'+todate+'"')
            mem1 = attendance.objects.filter(date__range=[fromdate, todate]).filter(user_id=st_id)
        return render(request, 'Staff_attendancesort.html',{'mem1':mem1,'mem':mem})
    else:
        return redirect('/')
    

def Staff_reportissues(request):
    if 'st_id' in request.session:
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=st_id)
        return render(request,'Staff_reportissues.html',{'mem':mem})
    else:
        return redirect('/')

def Staff_reportedissue(request):
    if 'st_id' in request.session:
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=st_id)
        var=reported_issue.objects.filter(reporter_id=st_id).order_by("-id")
        return render(request,'Staff_reportedissue.html',{'mem':mem,'var':var})
    else:
        return redirect('/')

def Staff_reportanissue(request):
    if 'st_id' in request.session:
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=st_id)
        ad_id = designation.objects.get(designation="manager")
        if request.method == 'POST':
            
            vars = reported_issue()
            vars.issue=request.POST.get('report')
            vars.reported_date=datetime.now()
            vars.reported_to_id=ad_id.id
            vars.reporter_id=st_id
            vars.status='pending'
            vars.save()
            return redirect('Staff_reportissues')
        else:
             return render(request,'Staff_reportanissue.html',{'mem':mem})
        
            
       
    else:
        return redirect('/')

def Staff_issuereportsstudents(request):
    if 'st_id' in request.session:
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=st_id)
        var=reported_issue.objects.filter(reported_to_id=st_id).order_by("-id")
        return render(request,'Staff_issuereportsstudents.html',{'mem':mem,'var':var})
    else:
            return redirect('/')

def Staffreplyview(request,id):
    if 'st_id' in request.session:
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=st_id)
        rid=request.GET.get('rid')
        mem1=reported_issue.objects.filter(id=id)
        
        return render(request, 'Staffreplyview.html',{'mem1':mem1,'mem':mem})
    else:
        return redirect('/')

def Staffissuereply(request,id):
    if 'st_id' in request.session:
        if request.session.has_key('st_id'):
            st_id = request.session['st_id']
        else:
            return redirect('/')
        st_id = user_registration.objects.filter(id=st_id)
        if request.method == 'POST':
            v = reported_issue.objects.get(id=id)
            v.reply=request.POST.get('reply')
            v.save()
        return redirect('Staff_reportissues')

    else:
        return redirect('/')


def reset_password(request):
    if request.method == "POST":
        email_id = request.POST.get('email')
        access_user_data = user_registration.objects.filter(email=email_id).exists()
        if access_user_data:
            _user = user_registration.objects.get(email=email_id)
            password = random.SystemRandom().randint(100000, 999999)

            _user.password = password
            # subject = 'iNFOX Technologies your authentication data updated\n'
            # message = 'Password Reset Successfully\n\nYour login details are below\n\nUsername : ' + str(email) + '\n\nPassword : ' + str(password) + \
            #     '\n\nYou can login this details'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [email_id, ]
            # send_mail(subject, message, email_from,
            #           recipient_list, fail_silently=False)

            _user.save()
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
       
        
        # subject = 'Greetings from iNFOX TECHNOLOGIES'
        # message = 'Congratulations,\n You have successfully registered with iNFOX TECHNOLOGIES.\nfollowing is your login credentials for taking aptitude test\nusername :'+str(email_id)+'\npassword :'+str(passw)+'\n'
        # email_from = settings.EMAIL_HOST_USER
        
        # recipient_list = [email_id, ]
        # send_mail(subject,message , email_from, [recipient_list], fail_silently=True)
        msg_success = "Registration successfully"
        abc = user_registration.objects.get(id=a.id)
        newps = request.POST["password"]
        cmps = request.POST["conpassword"]
        if newps == cmps:
            abc.password = request.POST.get('conpassword')
            abc.save()
        else:
            msg_error = "password missmatch error"
            return render(request, 'Registration_form.html',{'msg_error':msg_error})
        return render(request, 'Registration_form.html',{'msg_success': msg_success,'bat':bat})
    return render(request, 'Registration_form.html',{'bat':bat})