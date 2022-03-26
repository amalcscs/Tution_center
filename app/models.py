from xmlrpc.client import boolean
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class batch(models.Model):
    batch = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.designation


class designation(models.Model):
    batch = models.ForeignKey(
        batch, on_delete=models.DO_NOTHING, related_name='departmentbranch', null=True, blank=True)
    designation = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.designation


class user_registration(models.Model):
    designation = models.ForeignKey(designation, on_delete=models.DO_NOTHING,
                                    related_name='userregistrationdesignation', null=True, blank=True)
    batch = models.ForeignKey(batch, on_delete=models.DO_NOTHING,
                               related_name='userregistrationbatch', null=True, blank=True)
    
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
    startdate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    enddate = models.DateField(
        auto_now_add=False, auto_now=False,  null=True, blank=True)
    status = models.CharField(max_length=240, null=True, default='')
   

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