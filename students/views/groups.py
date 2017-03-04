# _*_ coding: utf-8 _*_

from django.shortcuts import render

from django.http import HttpResponse


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
