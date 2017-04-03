# _*_ coding: utf-8 _*_

from django.shortcuts import render

from django.http import HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.exams import Exam


    # Views for Groups

def exams_list(request):
    exams = Exam.objects.all()

    # try to order exams list

    order_by = request.GET.get('order_by', '')
    if order_by in ('date', 'student_group', 'location', 'title'):
        exams = exams.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            exams = exams.reverse()

    else:
        exams = exams.order_by('title')

    # paginator groups

    paginator = Paginator(exams, 3)
    page = request.GET.get('page')
    try:
        exams = paginator.page(page)
    except PageNotAnInteger:
        # If page not integer, deliver first page
        exams = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        exams = paginator.page(paginator.num_pages)

    return render(request, 'students/exam_list.html', {'exams': exams})


def exams_add(request):
    return HttpResponse('<h1>Exam Add Form</h1>')


def exams_edit(request, title):
    return HttpResponse('<h1> Edit Exam %s</h1>' % title)


def exams_delete(request, title):
    return HttpResponse('<h1>Delete Exam %s</h1>' % title)