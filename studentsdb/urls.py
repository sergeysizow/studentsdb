"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from students.views import students, groups, journal, exams, contact_admin
from students.views.students import StudentAddView, StudentUpdateView, StudentDeleteView
from students.views.groups import GroupAddView, GroupUpdateView, GroupDeleteView
from students.views.exams import ExamAddView, ExamUpdateView, ExamDeleteView
from students.views.journal import JournalView


from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # Students url
    url(r'^$', students.students_list, name='home'),
    url(r'^students/add/$', StudentAddView.as_view(), name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<pk>\d+)/delete/$', StudentDeleteView.as_view(), name='students_delete'),

    # Groups url
    url(r'^groups$', groups.groups_list, name='groups'),
    url(r'^groups/add/$', GroupAddView.as_view(), name='groups_add'),
    url(r'^groups/(?P<pk>\d+)/edit/$', GroupUpdateView.as_view(), name='groups_edit'),
    url(r'^groups/(?P<pk>\d+)/delete/$', GroupDeleteView.as_view(), name='groups_delete'),

    # Exams url
    url(r'^exams$', exams.exams_list, name='exams'),
    url(r'^exams/add/$', ExamAddView.as_view(), name='exams_add'),
    url(r'^exams/(?P<pk>\d+)/edit/$', ExamUpdateView.as_view(), name='exams_edit'),
    url(r'^exams/(?P<pk>\d+)/delete/$', ExamDeleteView.as_view(), name='exams_delete'),

    # Other url
    url(r'^journal/(?P<pk>\d+)?/?$', JournalView.as_view(), name='journal'),
    url(r'^admin/', include(admin.site.urls)),

    # Contact admin form
    url(r'^contact-admin/$', contact_admin.contact_admin, name='contact_admin'),
    # url(r'^contact-admin/$', ContactView.as_view()),
    # url(r'^contact-admin/$', include('contact_form.urls')),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    # serve files from media folder
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
