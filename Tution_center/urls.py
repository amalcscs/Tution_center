
from django.contrib import admin
from django.urls import re_path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import re_path
from app import views

urlpatterns = [
    re_path(r'^$', views.login, name='login'),
    re_path(r'^Staff_logout/$', views.Staff_logout, name='Staff_logout'),
    re_path(r'^reset_password/$', views.reset_password, name='reset_password'),
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
    re_path(r'^Registration/$', views.Registration_form, name='Registration_form'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
