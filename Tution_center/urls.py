
from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from app import views


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'^$', views.login, name='login'),
    re_path(r'^reset_password/$', views.reset_password, name='reset_password'),
    re_path(r'^Registration/$', views.Registration_form, name='Registration_form'),

#*******************************************Staff module*****************************************************
#*******************************************     Amal   *****************************************************

    re_path(r'^Staff_logout/$', views.Staff_logout, name='Staff_logout'),
    re_path(r'^Staff_index/$', views.Staff_index, name='Staff_index'),
    re_path(r'^Staff_accsetting/$', views.Staff_accsetting, name='Staff_accsetting'),
    re_path(r'^Staff_accsettingimagechange/(?P<id>\d+)/$', views.Staff_accsettingimagechange, name='Staff_accsettingimagechange'),
    re_path(r'^Staff_changepwd/$', views.Staff_changepwd, name='Staff_changepwd'),
    re_path(r'^Staff_dashboard/$', views.Staff_dashboard, name='Staff_dashboard'),
    re_path(r'^Staff_attendance/$', views.Staff_attendance, name='Staff_attendance'),
    re_path(r'^Staff_attandance/$', views.Staff_attendancesort, name='Staff_attendancesort'),
    re_path(r'^Staff_reportissues/$', views.Staff_reportissues, name='Staff_reportissues'),
    re_path(r'^Staff_reportedissue/$', views.Staff_reportedissue, name='Staff_reportedissue'),
    re_path(r'^Staff_reportanissue/$', views.Staff_reportanissue, name='Staff_reportanissue'),
    re_path(r'^Staff_issuereportsstudents/$', views.Staff_issuereportsstudents, name='Staff_issuereportsstudents'),
    re_path(r'^Staffreplyview/(?P<id>\d+)/$', views.Staffreplyview, name='Staffreplyview'),
    re_path(r'^Staffissuereply/(?P<id>\d+)/$', views.Staffissuereply, name='Staffissuereply'),
    re_path(r'^RegistrationUsers_Admin/$', views.RegistrationUsers_Admin, name='RegistrationUsers_Admin'),
    re_path(r'^RegistrationUser_Adminsave/(?P<id>\d+)/$', views.RegistrationUser_Adminsave, name='RegistrationUser_Adminsave'),
    re_path(r'^RegistrationAdminUser_delete/(?P<id>\d+)/$', views.RegistrationAdminUser_delete, name='RegistrationAdminUser_delete'),
    re_path(r'^RegistrationAdminUsers_update/(?P<id>\d+)/$', views.RegistrationAdminUsers_update, name='RegistrationAdminUsers_update'),
    re_path(r'^RegistrationAdminUsers_updatessave/(?P<id>\d+)/$', views.RegistrationAdminUsers_updatessave, name='RegistrationAdminUsers_updatessave'),


#*******************************************    Subeesh     ************************************************

    re_path(r'^Staff_leave/$', views.Staff_leave, name='Staff_leave'),
    re_path(r'^Staff_Student_det/$', views.Staff_Student_det, name='Staff_Student_det'),
    re_path(r'^Staff_apply_leave/$', views.Staff_apply_leave, name='Staff_apply_leave'),
    re_path(r'^Staff_Req_leave/$', views.Staff_Req_leave, name='Staff_Req_leave'),
    re_path(r'^Staff_studentsleave_table/$', views.Staff_studentsleave_table, name='Staff_studentsleave_table'),
    re_path(r'^Staff_current_students/$', views.Staff_current_students, name='Staff_current_students'),
    re_path(r'^Staff_previous_students/$', views.Staff_previous_students, name='Staff_previous_students'),

    re_path(r'^Staff_progress_report/$', views.Staff_progress_report, name='Staff_progress_report'),
    re_path(r'^Staff_progress_report_add/$', views.Staff_progress_report_add, name='Staff_progress_report_add'),
    re_path(r'^Staff_student_dashboard/(?P<id>\d+)/$', views.Staff_student_dashboard, name='Staff_student_dashboard'),
    re_path(r'^Staff_previous_student_dashboard/(?P<id>\d+)/$', views.Staff_previous_student_dashboard, name='Staff_previous_student_dashboard'),
    re_path(r'^Staff_progress_report_show/$', views.Staff_progress_report_show, name='Staff_progress_report_show'),
    re_path(r'^Staff_rejected_leave/(?P<id>\d+)/$', views.Staff_rejected_leave, name='Staff_rejected_leave'),
    re_path(r'^Staff_accepted_leave/(?P<id>\d+)/$', views.Staff_accepted_leave, name='Staff_accepted_leave'),
    re_path(r'^Staff_accepted_leave/(?P<id>\d+)/$', views.Staff_accepted_leave, name='Staff_accepted_leave'),

#********************************************Student module**************************************************
#*******************************************      Anwar    **************************************************
    re_path(r'^Student_logout/$', views.Student_logout, name='Student_logout'),
    re_path(r'^Student_index/$', views.Student_index, name='Student_index'),
    re_path(r'^Student_profiledash/$', views.Student_profiledash, name='Student_profiledash'),
    re_path(r'^Student_attendance/$', views.Student_attendance, name='Student_attendance'),
    re_path(r'^Student_attendancesort/$', views.Student_attendancesort, name='Student_attendancesort'),
    re_path(r'^Student_reportissues/$', views.Student_reportissues, name='Student_reportissues'),
    re_path(r'^Student_reportissue1/$', views.Student_reportissue1, name='Student_reportissue1'),
    re_path(r'^Student_reportissue2/$', views.Student_reportissue2, name='Student_reportissue2'),
    re_path(r'^Studentreportsuccess/$', views.Studentreportsuccess, name='Studentreportsuccess'),
    re_path(r'^Student_reportissuereply(?P<id>\d+)/$', views.Student_reportissuereply, name='Student_reportissuereply'),

    re_path(r'^Student_accsetting/$', views.Student_accsetting, name='Student_accsetting'),
    re_path(r'^Student_accsettingimagechange/(?P<id>\d+)/$', views.Student_accsettingimagechange, name='Student_accsettingimagechange'),
    re_path(r'^Student_changepwd/$', views.Student_changepwd, name='Student_changepwd'),  

#*******************************************      Akhil     *************************************************

    re_path(r'^Student_index/$', views.Student_index, name='Student_index'),
    re_path(r'^Student_applyleave_cards/$', views.Student_applyleave_cards, name='Student_applyleave_cards'),
    re_path(r'^Student_leavereq/$', views.Student_leavereq, name='Student_leavereq'),
    re_path(r'^Student_reqedleave/$', views.Student_reqedleave, name='Student_reqedleave'),
    re_path(r'^Student_progressreport/$', views.Student_progressreport, name='Student_progressreport'),
    re_path(r'^Student_leaverejected/(?P<id>\d+)/$', views.Student_leaverejected, name='Student_leaverejected'),

    
#**********************************************Manager module**************************************************
#**********************************************      Anwar   **************************************************

    re_path(r'^Man_index/$', views.Man_index, name='Man_index'),
    re_path(r'^Man_logout/$', views.Man_logout, name='Man_logout'),
    re_path(r'^Man_attendance/$',views.man_page1,name='man_page1'),
    re_path(r'^Man_attendanceshow/$',views.man_page3,name='man_page3'),
    re_path(r'^man_desi$',views.man_desi,name='man_desi'),
    re_path(r'^man_emp$',views.man_emp,name='man_emp'),

#*********************************************   Nimisha  **************************************************

    re_path(r'^MAN_Academic/$', views.MAN_Academic,
            name='MAN_Academic'),
    re_path(r'^MAN_ViewClass/$', views.MAN_ViewClass,
        name='MAN_ViewClass'),
    re_path(r'^MAN_UpdateClass/(?P<id>\d+)/$', views.MAN_UpdateClass,
        name='MAN_UpdateClass'),
    re_path(r'^MAN_Update_Classsave/(?P<id>\d+)/$', views.MAN_Update_Classsave,
        name='MAN_Update_Classsave'),
    re_path(r'^MAN_deleteclass/(?P<id>\d+)/$', views.MAN_deleteclass,
        name='MAN_deleteclass'),

#*********************************************  Meenu  ******************************************************

 #------------------staff---------------#

    re_path(r'^Manager_staff/$',views.Manager_staff, name="Manager_staff"),  
    re_path(r'^Manager_currentstaffdetails/$',views.Manager_currentstaffdetails, name="Manager_currentstaffdetails"),   
    re_path(r'^Manager_previousstaffdetails/$',views.Manager_previousstaffdetails, name="Manager_previousstaffdetails"), 
    re_path(r'^Manager_staffprofile/(?P<id>\d+)/$',views.Manager_staffprofile, name="Manager_staffprofile"), 
    re_path(r'^Manager_attendancesearch/(?P<id>\d+)/$',views.Manager_attendancesearch, name="Manager_attendancesearch"),   
    re_path(r'^Manager_attendancesort/(?P<id>\d+)/$',views.Manager_attendancesort, name="Manager_attendancesort"),   

#-------------------student------------#

    re_path(r'^Manager_student/$',views.Manager_student, name="Manager_student"),
    re_path(r'^Manager_currentstudentdetails/$',views.Manager_currentstudentdetails, name="Manager_currentstudentdetails"),  
    re_path(r'^Manager_previousstudentdetails/$',views.Manager_previousstudentdetails, name="Manager_previousstudentdetails"),  
    re_path(r'^Manager_studentprofile/(?P<id>\d+)/$',views.Manager_studentprofile, name="Manager_studentprofile"),  
    re_path(r'^Manager_student_attendancesearch/(?P<id>\d+)/$',views.Manager_student_attendancesearch, name="Manager_student_attendancesearch"),   
    re_path(r'^Manager_sort/(?P<id>\d+)/$',views.Manager_sort, name="Manager_sort"),   

#--------------Leave Request-------------#
    re_path(r'^Manager_leaverequest_staff/$',views.Manager_leaverequest_staff, name="Manager_leaverequest_staff"),
    re_path(r'^Manager_apply_leave/$',views.Manager_apply_leave, name="Manager_apply_leave"),
    re_path(r'^Manager_requestleave/$',views.Manager_requestleave, name="Manager_requestleave"),
    re_path(r'^Manager_staffleave/$',views.Manager_staffleave, name="Manager_staffleave"),
    re_path(r'^Manager_rejected_leave/(?P<id>\d+)/$',views.Manager_rejected_leave, name="Manager_rejected_leave"),
    re_path(r'^Manager_accepted_leave/(?P<id>\d+)/$',views.Manager_accepted_leave, name="Manager_accepted_leave"),

#---------------academics-----------#
    re_path(r'^Manager_academics/$',views.Manager_academics,name="Manager_academics"),
    re_path(r'^Manager_academics_viewbatch/$',views.Manager_academics_viewbatch,name="Manager_academics_viewbatch"),
    re_path(r'^Manager_academics_delete/(?P<id>\d+)/$',views.Manager_academics_delete,name="Manager_academics_delete") , 
    re_path(r'^Manager_academics_update/(?P<id>\d+)/$', views.Manager_academics_update,name='Manager_academics_update'),
    re_path(r'^Manager_academics_updatesave/(?P<id>\d+)/$', views.Manager_academics_updatesave,name='Manager_academics_updatesave'),

#******************************************   Akhil   *************************************************

    re_path(r'^MAN_Report/$', views.MAN_Report, name='MAN_Report'),
    # re_path(r'^MAN_Reportedissue$', views.MAN_Reportedissue, name='MAN_Reportedissue'),
    re_path(r'^MAN_ReportedissueShow/(?P<id>\d+)/$', views.MAN_ReportedissueShow, name='MAN_ReportedissueShow'),
    re_path(r'^MAN_rep/(?P<id>\d+)/$', views.MAN_rep, name='MAN_rep'),
    re_path(r'^MAN_ReportedissueShow1/(?P<id>\d+)/$',views.MAN_ReportedissueShow1, name='MAN_ReportedissueShow1'),
    re_path(r'^MAN_manager_report/$', views.MAN_manager_report, name='MAN_manager_report'),
    re_path(r'^MAN_Reportissue/$', views.MAN_Reportissue, name='MAN_Reportissue'),
    re_path(r'^MAN_reportsuccess/$', views.MAN_reportsuccess, name='MAN_reportsuccess'),
    re_path(r'^MAN_manger_reportedissues/$', views.MAN_manger_reportedissues, name='MAN_manger_reportedissues'),
    re_path(r'^MAN_manger_reportedissues1/(?P<id>\d+)/$', views.MAN_manger_reportedissues1, name='MAN_manger_reportedissues1'),


#*******************************************  Sharon   *****************************************

    re_path(r'^MAN_profile/$',views.MAN_profile, name="MAN_profile"),
    re_path(r'^MAN_registration/$',views.MAN_registration, name="MAN_registration"),
    re_path(r'^MAN_registrationstaff/$',views.MAN_registrationstaff, name="MAN_registrationstaff"),
    re_path(r'^MAN_registrationstudent/$',views.MAN_registrationstudent, name="MAN_registrationstudent"),
    re_path(r'^MAN_currentstaff/$',views.MAN_currentstaff, name="MAN_currentstaff"),
    re_path(r'^MAN_resignedstaff/$',views.MAN_resignedstaff, name="MAN_resignedstaff"),
    re_path(r'^MAN_currentstudent/$',views.MAN_currentstudent, name="MAN_currentstudent"),
    re_path(r'^MAN_resignedstudent/$',views.MAN_resignedstudent, name="MAN_resignedstudent"),
    re_path(r'^MAN_academics/$',views.MAN_academics, name="MAN_academics"),
    re_path(r'^MAN_batch/$',views.MAN_batch, name="MAN_batch"),
    re_path(r'^MAN_addbatch/$',views.MAN_addbatch, name="MAN_addbatch"),

    re_path(r'^MAN_changepwd/$', views.MAN_changepwd, name='MAN_changepwd'),
    re_path(r'^MAN_accsetting/$', views.MAN_accsetting, name='MAN_accsetting'),
    re_path(r'^MAN_accsettingimagechange/(?P<id>\d+)/$', views.MAN_accsettingimagechange, name='MAN_accsettingimagechange'),

#*************************************praveen************************
    re_path(r'^Man_Academic_Subject/$', views.Man_Academic_Subject,
                  name='Man_Academic_Subject'),
    re_path(r'^Man_AddSubject/$', views.Man_AddSubject,
                name='Man_AddSubject'),
    re_path(r'^Man_AddSubject_save/$', views.Man_AddSubject_save,
                name='Man_AddSubject_save'),

#**************************************subeesh**********************************
    re_path(r'^Man_ViewSubject/$', views.Man_ViewSubject,
                name='Man_ViewSubject'),
    re_path(r'^Man_UpdateSubject/(?P<id>\d+)/$', views.Man_UpdateSubject,
                name='Man_UpdateSubject'),
    re_path(r'^Man_UpdateSubject_save/(?P<id>\d+)/$', views.Man_UpdateSubject_save,
                name='Man_UpdateSubject_save'),
    re_path(r'^Man_deletesubject/(?P<id>\d+)/$', views.Man_deletesubject,
                name='Man_deletesubject'),

    #***********************************anandhu*********************************

    re_path(r'^MAN_AcademicClass/$', views.MAN_AcademicClass, name='MAN_AcademicClass'),
    re_path(r'^MAN_AcademicAddClass/$', views.MAN_AcademicAddClass, name='MAN_AcademicAddClass'),
    re_path(r'^MAN_AcademicAddClasssave/$', views.MAN_AcademicAddClasssave, name='MAN_AcademicAddClasssave'),

#*********************Admin module******************************

#************************Akhil***************************

    re_path(r'^Admin_index/$', views.Admin_index, name='Admin_index'),
    re_path(r'^Admin_dashboard/$', views.Admin_dashboard, name='Admin_dashboard'),
    re_path(r'^superadmin_logout/$', views.superadmin_logout, name='superadmin_logout'),
    re_path(r'^superadmin_changepwd/$', views.superadmin_changepwd, name='superadmin_changepwd'),

    #************************Nimisha***************************


    re_path(r'^Admin_index/$', views.Admin_index,
            name='Admin_index'),
      #-------Academic------
      re_path(r'^Admin_Academic/$', views.Admin_Academic,
            name='Admin_Academic'),
      re_path(r'^Admin_Academic_Class/$', views.Admin_Academic_Class,
                  name='Admin_Academic_Class'),
      re_path(r'^Admin_AddClass/$', views.Admin_AddClass,
                  name='Admin_AddClass'),
      re_path(r'^Admin_ViewClass/$', views.Admin_ViewClass,
                  name='Admin_ViewClass'),
      re_path(r'^Admin_add_classsave/$', views.Admin_add_classsave,
                  name='Admin_add_classsave'),
      re_path(r'^Admin_deleteclass/(?P<id>\d+)/$', views.Admin_deleteclass,
                  name='Admin_deleteclass'),
      re_path(r'^Admin_UpdateClass/(?P<id>\d+)/$', views.Admin_UpdateClass,
                  name='Admin_UpdateClass'),
      re_path(r'^Admin_Update_Classsave/(?P<id>\d+)/$', views.Admin_Update_Classsave,
                  name='Admin_Update_Classsave'),
      re_path(r'^Admin_Academic_Subject/$', views.Admin_Academic_Subject,
                  name='Admin_Academic_Subject'),
      re_path(r'^Admin_AddSubject/$', views.Admin_AddSubject,
                  name='Admin_AddSubject'),
      re_path(r'^Admin_AddSubject_save/$', views.Admin_AddSubject_save,
                  name='Admin_AddSubject_save'),
      re_path(r'^Admin_ViewSubject/$', views.Admin_ViewSubject,
                  name='Admin_ViewSubject'),
      re_path(r'^Admin_UpdateSubject/(?P<id>\d+)/$', views.Admin_UpdateSubject,
                  name='Admin_UpdateSubject'),
      re_path(r'^Admin_UpdateSubject_save/(?P<id>\d+)/$', views.Admin_UpdateSubject_save,
                  name='Admin_UpdateSubject_save'),
      re_path(r'^Admin_deletesubject/(?P<id>\d+)/$', views.Admin_deletesubject,
                  name='Admin_deletesubject'),
      
      #-----Attendance-------

      re_path(r'^Admin_Attendance/$', views.Admin_Attendance,
                  name='Admin_Attendance'),
      re_path(r'^Admin_Attendance_Show/$', views.Admin_Attendance_Show,
                  name='Admin_Attendance_Show'),
      re_path(r'^Admin_At_Designation/$', views.Admin_At_Designation,
                  name='Admin_At_Designation'),
      re_path(r'^Admin_At_Name/$', views.Admin_At_Name,
                  name='Admin_At_Name'),

      #---------Reported issues-------
      re_path(r'^Admin_Reportedissues_Card/$', views.Admin_Reportedissues_Card,
                  name='Admin_Reportedissues_Card'),
      re_path(r'^Admin_Reportedissues/(?P<id>\d+)/$', views.Admin_Reportedissues,
                  name='Admin_Reportedissues'),
      re_path(r'^Admin_Reportedissues_Show/(?P<id>\d+)/$', views.Admin_Reportedissues_Show,
                  name='Admin_Reportedissues_Show'),
      re_path(r'^Admin_Reportedissuetomanager/(?P<id>\d+)/$', views.Admin_Reportedissuetomanager,
                  name='Admin_Reportedissuetomanager'),
      re_path(r'^Adminreplyview/(?P<id>\d+)/$', views.Adminreplyview,
                  name='Adminreplyview'),
      re_path(r'^Adminissuereply/(?P<id>\d+)/$', views.Adminissuereply,
                  name='Adminissuereply'),

      #--------Leave--------

      re_path(r'^Admin_LeaveRequest/$', views.Admin_LeaveRequest,
                  name='Admin_LeaveRequest'),
      re_path(r'^Admin_acceptedManager_leave/(?P<id>\d+)/$', views.Admin_acceptedManager_leave,
                  name='Admin_acceptedManager_leave'),
      re_path(r'^Admin_rejectedManager_leave/(?P<id>\d+)/$', views.Admin_rejectedManager_leave, 
                  name='Admin_rejectedManager_leave'),

    #************************************Anandhu************************************
      re_path(r'^Registration_Admin/$', views.Registration_Admin, name='Registration_Admin'),
      re_path(r'^RegistrationStaff_Admin/(?P<id>\d+)/$', views.RegistrationStaff_Admin, name='RegistrationStaff_Admin'),
      re_path(r'^RegistrationStudent_Admin/(?P<id>\d+)/$', views.RegistrationStudent_Admin, name='RegistrationStudent_Admin'),
      re_path(r'^RegistrationCurrentStaff_Admin/$', views.RegistrationCurrentStaff_Admin, name='RegistrationCurrentStaff_Admin'),
      re_path(r'^RegistrationCurrentStaff_Adminsave/(?P<id>\d+)/$', views.RegistrationCurrentStaff_Adminsave, name='RegistrationCurrentStaff_Adminsave'),
      re_path(r'^RegistrationCurrentStaffAdmin_update/(?P<id>\d+)/$', views.RegistrationCurrentStaffAdmin_update, name='RegistrationCurrentStaffAdmin_update'),
      re_path(r'^RegistrationCurrentStaffAdmin_updatessave/(?P<id>\d+)/$', views.RegistrationCurrentStaffAdmin_updatessave, name='RegistrationCurrentStaffAdmin_updatessave'),
      re_path(r'^RegistrationCurrentStaffAdmin_delete/(?P<id>\d+)/$', views.RegistrationCurrentStaffAdmin_delete, name='RegistrationCurrentStaffAdmin_delete'),
      re_path(r'^RegistrationResignedStaffAdmin_update/(?P<id>\d+)/$', views.RegistrationResignedStaffAdmin_update, name='RegistrationResignedStaffAdmin_update'),
      re_path(r'^RegistrationResignedStaffAdmin_updatessave/(?P<id>\d+)/$', views.RegistrationResignedStaffAdmin_updatessave, name='RegistrationResignedStaffAdmin_updatessave'),
      re_path(r'^RegistrationResignedStaffAdmin_delete/$', views.RegistrationResignedStaffAdmin_delete, name='RegistrationResignedStaffAdmin_delete'),
      re_path(r'^RegistrationResignedStaff_Admin/$', views.RegistrationResignedStaff_Admin, name='RegistrationResignedStaff_Admin'),
      re_path(r'^RegistrationCurrentStudent_Admin/$', views.RegistrationCurrentStudent_Admin, name='RegistrationCurrentStudent_Admin'),
      re_path(r'^RegistrationCurrentStudent_Adminsave/(?P<id>\d+)/$', views.RegistrationCurrentStudent_Adminsave, name='RegistrationCurrentStudent_Adminsave'),
      re_path(r'^RegistrationPreviousstudent_Admin/$', views.RegistrationPreviousstudent_Admin, name='RegistrationPreviousstudent_Admin'),

      re_path(r'^Staff_Admin/$', views.Staff_Admin, name='Staff_Admin'),
      re_path(r'^StaffCurrentstaff_Admin/$', views.StaffCurrentstaff_Admin, name='StaffCurrentstaff_Admin'),
      re_path(r'^StaffPreviousstaff_Admin/$', views.StaffPreviousstaff_Admin, name='StaffPreviousstaff_Admin'),
      re_path(r'^StaffCurrentstaffProfile_Admin/(?P<id>\d+)/$', views.StaffCurrentstaffProfile_Admin, name='StaffCurrentstaffProfile_Admin'),
      re_path(r'^StaffPreviousstaffProfile_Admin/(?P<id>\d+)/$', views.StaffPreviousstaffProfile_Admin, name='StaffPreviousstaffProfile_Admin'),
      re_path(r'^StaffCurrentstaffAttendance_Admin/(?P<id>\d+)/$', views.StaffCurrentstaffAttendance_Admin, name='StaffCurrentstaffAttendance_Admin'),
      re_path(r'^StaffCurrentstaffAttendanceSort_Admin/(?P<id>\d+)/$', views.StaffCurrentstaffAttendanceSort_Admin, name='StaffCurrentstaffAttendanceSort_Admin'),
      re_path(r'^StaffPreviousstaffAttendance_Admin/(?P<id>\d+)/$', views.StaffPreviousstaffAttendance_Admin, name='StaffPreviousstaffAttendance_Admin'),
      re_path(r'^StaffPreviousstaffAttendanceSort_Admin/(?P<id>\d+)/$', views.StaffPreviousstaffAttendanceSort_Admin, name='StaffPreviousstaffAttendanceSort_Admin'),
    
      re_path(r'^StaffCurrentstaffPerformance_Admin/(?P<id>\d+)/$', views.StaffCurrentstaffPerformance_Admin, name='StaffCurrentstaffPerformance_Admin'),
      re_path(r'^StaffCurrentstaffPerformance_Adminsave/(?P<id>\d+)/$', views.StaffCurrentstaffPerformance_Adminsave, name='StaffCurrentstaffPerformance_Adminsave'),

      re_path(r'^StaffPreviousstaffPerformance_Admin/(?P<id>\d+)/$', views.StaffPreviousstaffPerformance_Admin, name='StaffPreviousstaffPerformance_Admin'),
      re_path(r'^StaffPreviousstaffPerformance_Adminsave/(?P<id>\d+)/$', views.StaffPreviousstaffPerformance_Adminsave, name='StaffPreviousstaffPerformance_Adminsave'),

      re_path(r'^StudentCurrentstudentPerformance_Admin/(?P<id>\d+)/$', views.StudentCurrentstudentPerformance_Admin, name='StudentCurrentstudentPerformance_Admin'),
      re_path(r'^StudentCurrentstudentPerformance_Adminsave/(?P<id>\d+)/$', views.StudentCurrentstudentPerformance_Adminsave, name='StudentCurrentstudentPerformance_Adminsave'),

      re_path(r'^StudentPreviousstudentPerformance_Admin/(?P<id>\d+)/$', views.StudentPreviousstudentPerformance_Admin, name='StudentPreviousstudentPerformance_Admin'),
      re_path(r'^StudentPreviousstudentPerformance_Adminsave/(?P<id>\d+)/$', views.StudentPreviousstudentPerformance_Adminsave, name='StudentPreviousstudentPerformance_Adminsave'),

      re_path(r'^Student_Admin/$', views.Student_Admin, name='Student_Admin'),
      re_path(r'^StudentCurrentstudent_Admin/$', views.StudentCurrentstudent_Admin, name='StudentCurrentstudent_Admin'),
      re_path(r'^StudentPreviousstudent_Admin/$', views.StudentPreviousstudent_Admin, name='StudentPreviousstudent_Admin'),
      re_path(r'^StudentCurrentstudentProfile_Admin/(?P<id>\d+)/$', views.StudentCurrentstudentProfile_Admin, name='StudentCurrentstudentProfile_Admin'),
      re_path(r'^StudentPreviousstudentProfile_Admin/(?P<id>\d+)/$', views.StudentPreviousstudentProfile_Admin, name='StudentPreviousstudentProfile_Admin'),
      re_path(r'^StudentCurrentstudentAttendance_Admin/(?P<id>\d+)/$', views.StudentCurrentstudentAttendance_Admin, name='StudentCurrentstudentAttendance_Admin'),
      re_path(r'^StudentCurrentstudentAttendanceSort_Admin/(?P<id>\d+)/$', views.StudentCurrentstudentAttendanceSort_Admin, name='StudentCurrentstudentAttendanceSort_Admin'),
      re_path(r'^StudentPreviousstudentAttendance_Admin/(?P<id>\d+)/$', views.StudentPreviousstudentAttendance_Admin, name='StudentPreviousstudentAttendance_Admin'),
      re_path(r'^StudentPreviousstudentAttendanceSort_Admin/(?P<id>\d+)/$', views.StudentPreviousstudentAttendanceSort_Admin, name='StudentPreviousstudentAttendanceSort_Admin'),

      re_path(r'^Academic_Admin/$', views.Academic_Admin, name='Academic_Admin'),
      re_path(r'^AcademicBatch_Admin/$', views.AcademicBatch_Admin, name='AcademicBatch_Admin'),
      re_path(r'^AcademicAddBatch_Admin/$', views.AcademicAddBatch_Admin, name='AcademicAddBatch_Admin'),
      re_path(r'^AcademicAddBatch_Adminsave/$', views.AcademicAddBatch_Adminsave, name='AcademicAddBatch_Adminsave'),
      re_path(r'^AcademicAddBatchUpdate_Admin/(?P<id>\d+)/$', views.AcademicAddBatchUpdate_Admin, name='AcademicAddBatchUpdate_Admin'),
      re_path(r'^AcademicAddBatchUpdate_Adminsave/(?P<id>\d+)/$', views.AcademicAddBatchUpdate_Adminsave, name='AcademicAddBatchUpdate_Adminsave'),
      re_path(r'^AcademicViewBatch_Admin/$', views.AcademicViewBatch_Admin, name='AcademicViewBatch_Admin'),
      re_path(r'^AcademicAddBatch_Admindelete/(?P<id>\d+)/$', views.AcademicAddBatch_Admindelete, name='AcademicAddBatch_Admindelete'),
    
      re_path(r'^RegistrationCurrentStudentAdmin_update/(?P<id>\d+)/$', views.RegistrationCurrentStudentAdmin_update, name='RegistrationCurrentStudentAdmin_update'),
      re_path(r'^RegistrationCurrentStudent_updatessave/(?P<id>\d+)/$', views.RegistrationCurrentStudent_updatessave, name='RegistrationCurrentStudent_updatessave'),
      re_path(r'^RegistrationCurrentStudentAdmin_delete/(?P<id>\d+)/$', views.RegistrationCurrentStudentAdmin_delete, name='RegistrationCurrentStudentAdmin_delete'),

      re_path(r'^RegistrationPreviousstudentAdmin_update/(?P<id>\d+)/$', views.RegistrationPreviousstudentAdmin_update, name='RegistrationPreviousstudentAdmin_update'),
      re_path(r'^RegistrationPreviousstudentAdmin_updatessave/(?P<id>\d+)/$', views.RegistrationPreviousstudentAdmin_updatessave, name='RegistrationPreviousstudentAdmin_updatessave'),
      re_path(r'^RegistrationPreviousstudentAdmin_delete/(?P<id>\d+)/$', views.RegistrationPreviousstudentAdmin_delete, name='RegistrationPreviousstudentAdmin_delete'),

    #***************************Account module***************************

    #******************************Subeesh******************************

      re_path(r'^Acc_index/$', views.Acc_index, name='Acc_index'),
      re_path(r'^account_dashboard/$', views.account_dashboard, name='account_dashboard'),
      re_path(r'^Account_Student_det/$', views.Account_Student_det, name='Account_Student_det'),
      re_path(r'^Account_previous_students/$', views.Account_previous_students, name='Account_previous_students'),
      re_path(r'^account_changepassword/$', views.account_changepassword, name='account_changepassword'),
      re_path(r'^Acc_current_students/$', views.Acc_current_students, name='Acc_current_students'),
      re_path(r'^account_accsetting/$', views.account_accsetting, name='account_accsetting'),
      re_path(r'^account_logout/$', views.account_logout, name='account_logout'),
      re_path(r'^Acc_current_students_payment/(?P<id>\d+)/$', views.Acc_current_students_payment, name='Acc_current_students_payment'),
      re_path(r'^account_accsettingimagechange/(?P<id>\d+)/$', views.account_accsettingimagechange, name='account_accsettingimagechange'),

      #**********************************sharon***************************
      re_path(r'^account_leaverequest/$',views.account_leaverequest, name="account_leaverequest"),
      re_path(r'^account_applyleave/$',views.account_applyleave, name="account_applyleave"),
      re_path(r'^account_requestedleave/$',views.account_requestedleave, name="account_requestedleave"),
      re_path(r'^account_issues/$',views.account_issues, name="account_issues"),
      re_path(r'^account_reportedissue/$',views.account_reportedissue, name="account_reportedissue"),
      re_path(r'^account_report_an_issue/$',views.account_report_an_issue, name="account_report_an_issue"),
      re_path(r'^account_issuereply/(?P<id>\d+)/$',views.account_issuereply, name="account_issuereply"),


      re_path(r'^Accounts_Staff$', views.Accounts_Staff, name='Accounts_Staff'),
      re_path(r'^Accounts_CurrentStaff$', views.Accounts_CurrentStaff,name='Accounts_CurrentStaff'),
      re_path(r'^Accounts_CurrentStaffAddaccount/(?P<id>\d+)$', views.Accounts_CurrentStaffAddaccount,name='Accounts_CurrentStaffAddaccount'),
      re_path(r'^Accounts_CurrentStaffpayslip$', views.Accounts_CurrentStaffpayslip,name='Accounts_CurrentStaffpayslip'),    
      re_path(r'^accounts_acntpay$', views.accounts_acntpay, name='accounts_acntpay'),
      re_path(r'^accounts_paydetails/(?P<id>\d+)/(?P<tid>\d+)/$', views.accounts_paydetails,name='accounts_paydetails'),
      re_path(r'^accounts_print/(?P<id>\d+)/(?P<tid>\d+)/$', views.accounts_print,name='accounts_print'),
      re_path(r'^account_payment_details/(?P<id>\d+)$', views.account_payment_details,name='account_payment_details'),
      re_path(r'^account_payment_salary/(?P<id>\d+)$', views.account_payment_salary,name='account_payment_salary'),
      re_path(r'^account_payment_view/(?P<id>\d+)$', views.account_payment_view,name='account_payment_view'),
      re_path(r'^Account_staffprevious/$', views.Account_staffprevious, name='Account_staffprevious'),



]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
