# _*_ coding: utf-8 _*_

from django.shortcuts import render

from django.http import HttpResponse

from ..models import Student

# Views for Students

def students_list(request):
    students = Student.objects.all()

    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')


def students_edit(request, sid):  # sid= student id
    return HttpResponse('<h1>Edit Students %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


 
