# _*_ coding: utf-8 _*_

from django.shortcuts import render

from django.http import HttpResponse


# Views for Students

def students_list(request):
    students = (
        {'id': 1,
         'first_name': u'Дональд',
         'last_name': u'Трамп',
         'ticket': 6456,
         'image': 'img/tramp.jpg'},

        {'id': 2,
         'first_name': u'Володя',
         'last_name': u'Путін',
         'ticket': 6666,
         'image': 'img/putin.jpg'},

        {'id': 3,
         'first_name': u'Порошенко',
         'last_name': u'Петро',
         'ticket': 6589,
         'image': 'img/poroshenko.jpg'},

    )
    return render(request, 'students/students_list.html', {'students': students})


def students_add(request):
    return HttpResponse('<h1>Students Add Form</h1>')


def students_edit(request, sid):  # sid= student id
    return HttpResponse('<h1>Edit Students %s</h1>' % sid)


def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)


 
