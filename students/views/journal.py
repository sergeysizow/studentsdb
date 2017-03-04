# _*_ coding: utf-8 _*_

from django.shortcuts import render


    # Views for Journal

def journal_list(request):
    journal = (
        {'id': 1,
         'group': 304,
         'student': u'Трамп Д.'},

        {'id': 2,
         'group': 203,
         'student': u'Путін В.'},

        {'id': 3,
         'group': 104,
         'student': u'Порошенко П.'},
    )
    return render(request, 'students/journal_list.html', {'journal': journal})
