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


    # Views for Groups

def groups_list(request):
    groups = (
        {'id': 1,
         'group': 304,
         'leader': u'Трамп Д.'},

        {'id': 2,
         'group': 203,
         'leader': u'Путін В.'},

        {'id': 3,
         'group': 104,
         'leader': u'Порошенко П.'},
    )
    return render(request, 'students/groups_list.html', {'groups': groups})


def groups_add(request):
    return HttpResponse('<h1>Group Add Form</h1>')


def groups_edit(request, gid):  # gid= group id
    return HttpResponse('<h1> Edit Group %s</h1>' % gid)


def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
