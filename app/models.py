from xmlrpc.client import boolean
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class batch(models.Model):
    batch = models.CharField(max_length=100)
    description = models.CharField(max_length=100,default='')
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.batch


class designation(models.Model):
    batch = models.ForeignKey(
        batch, on_delete=models.DO_NOTHING, related_name='designationbatch', null=True, blank=True)
    designation = models.CharField(max_length=100)
    files=models.FileField(upload_to = 'images/', null=True, blank=True)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.designation


class subject(models.Model):
    batch = models.ForeignKey(batch,on_delete=models.DO_NOTHING,related_name='batchsubject',null=True,blank=True)
    subject = models.CharField(max_length=100)
    Rate = models.CharField(max_length=100,default='')
    logo = models.FileField(upload_to='images/', null=True, blank=True,default='')

    def __str__(self):
        return self.subject


class class_registration(models.Model):
    batch = models.ForeignKey(batch,on_delete=models.DO_NOTHING,related_name='batchclass',null=True,blank=True)
    class_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name


class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                                    related_name='userregistrationdesignation', null=True, blank=True)
    batch = models.ForeignKey(batch, on_delete=models.DO_NOTHING,
                               related_name='userregistrationbatch', null=True, blank=True)
    class_registration= models.ForeignKey(class_registration, on_delete=models.DO_NOTHING,
                                    related_name='class_registration', null=True, blank=True)
    subject = models.ForeignKey(subject, on_delete=models.SET_NULL,null=True, blank=True)
    fullname = models.CharField(max_length=240, null=True)
    fathername = models.CharField(max_length=240, null=True)
    mothername = models.CharField(max_length=240, null=True)
    dateofbirth = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    gender = models.CharField(max_length=240, null=True)
    presentaddress1 = models.CharField(max_length=240, null=True)
    presentaddress2 = models.CharField(max_length=240, null=True)
    presentaddress3 = models.CharField(max_length=240, null=True)
    pincode = models.CharField(max_length=240, null=True)
    district = models.CharField(max_length=240, null=True)
    state = models.CharField(max_length=240, null=True)
    country = models.CharField(max_length=240, null=True)
    permanentaddress1 = models.CharField(max_length=240, null=True)
    permanentaddress2 = models.CharField(max_length=240, null=True)
    permanentaddress3 = models.CharField(max_length=240, null=True)
    permanentpincode = models.CharField(max_length=240, null=True)
    permanentdistrict = models.CharField(max_length=240, null=True)
    permanentstate = models.CharField(max_length=240, null=True)
    permanentcountry = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    alternativeno = models.CharField(max_length=240, null=True)
    staff_id = models.CharField(max_length=240, null=True, default='')
    student_id = models.CharField(max_length=240, null=True, default='')
    email = models.EmailField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    idproof = models.FileField(upload_to='images/', null=True, blank=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)
    attitude = models.IntegerField(default='0')
    creativity = models.IntegerField(default='0')
    workperformance = models.IntegerField(default='0')
    joiningdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    dateofappointment = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    startdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')
    Std_id = models.IntegerField(default='0',null=True, blank=True)
    staff_id = models.IntegerField(default='0',null=True, blank=True)
    total_pay=models.IntegerField(default='0')
    payment_balance = models.IntegerField( default='0')
    account_no = models.CharField(max_length=200, null=True, default='')
    ifsc =  models.CharField(max_length=200, null=True, default='')
    bank_name = models.CharField(max_length=240, null=True, default='')
    bank_branch = models.CharField(max_length=240, null=True, default='')
    payment_status = models.CharField(max_length=200, null=True, default='')

    def __str__(self):
        return self.fullname


class attendance(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                             related_name='attendanceuser', null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    status = models.CharField(max_length=200)

    def __str__(self):
        return self.user


class reported_issue(models.Model):
    reporter = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                                 related_name='reported_issuereporter', null=True, blank=True)
    reported_to = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                                    related_name='reported_issuereported_to', null=True, blank=True)
    issue = models.TextField()
    reported_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    reply = models.TextField()
    status = models.CharField(max_length=200)
    def __str__(self):
        return self.reporter


class Leave(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,
                             related_name='leaveuser', null=True, blank=True)
    from_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    to_date = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    reason = models.TextField()
    leave_status = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    designation_id = models.CharField(max_length=200)
    leaveapprovedstatus = models.CharField(max_length=200)
    leave_rejected_reason = models.CharField(max_length=300)

class progressreport(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,null=True, blank=True)
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,null=True, blank=True)                        
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    subject = models.CharField(max_length=200)
    mark = models.CharField(max_length=200)

class payment(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING,null=True, blank=True)                        
    date = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    account_no = models.CharField(max_length=240,null=True,default='')
    ifsc = models.CharField(max_length=240,null=True,default='')
    branch = models.CharField(max_length=100,default='')
    payment = models.CharField(max_length=200)


class acntspayslip(models.Model):
    
    basic_salary = models.IntegerField()
    eno = models.CharField(max_length=100) 
    user_id = models.ForeignKey(user_registration, on_delete=models.DO_NOTHING, related_name='user',null=True,blank=True)
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING, related_name='desic',null=True,blank=True)
    batch =models.ForeignKey(batch, on_delete=models.DO_NOTHING, related_name='accbatch',null=True,blank=True)
    hra = models.IntegerField()
    conveyns = models.CharField(max_length=100)
    tax = models.IntegerField()
    incentives = models.IntegerField()
    fromdate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    todate = models.DateField(auto_now_add=False, auto_now=False,  null=True, blank=True)
    taxengine = models.CharField(max_length=100) 
    incometax = models.IntegerField() 
    uan = models.CharField(max_length=100) 
    pf = models.IntegerField() 
    esi = models.CharField(max_length=100)  
    pro = models.CharField(max_length=100) 
    leavesno = models.IntegerField() 
    pf_tax = models.IntegerField()
    delay = models.IntegerField()
    basictype =  models.CharField(max_length=255,default='')
    hratype = models.CharField(max_length=255,default='')
    contype = models.CharField(max_length=255,default='')
    protype = models.CharField(max_length=255,default='')
    instype = models.CharField(max_length=255,default='')
    deltype = models.CharField(max_length=255,default='')
    leatype = models.CharField(max_length=255,default='')
    pftype =  models.CharField(max_length=255,default='')
    esitype =  models.CharField(max_length=255,default='')