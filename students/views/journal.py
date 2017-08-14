# _*_ coding: utf-8 _*_

from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.base import TemplateView

from ..models.students import Student
from  ..models.monthjournal import MonthJournal


    # Views for Journal
"""
def journal_list(request):
    journal = Student.objects.all()

    return render(request, 'students/journal_list.html', {'journal': journal})

def students_list(request):
    students = Student.objects.all()

    # try to order students list

    order_by = request.GET.get('order_by', '')
    if order_by in ('last_name', 'first_name', 'ticket'):
        students = students.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            students = students.reverse()

    else:
        students = students.order_by('last_name')

    # paginator students

    paginator = Paginator(students, 3)
    page = request.GET.get('page')
    try:
        students = paginator.page(page)
    except PageNotAnInteger:
        # If page not integer, deliver first page
        students = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        students = paginator.page(paginator.num_pages)

    return render(request, 'students/students_list.html', {'students': students})
    """


class JournalView(TemplateView):
    template_name = 'journal/journal.html'

