# _*_ coding: utf-8 _*_
from datetime import date, datetime
from django.core.urlresolvers import reverse
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr
from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic.base import TemplateView

from ..models.students import Student
from ..models.monthjournal import MonthJournal
from ..util import paginate


# Views for Journal

class JournalView(TemplateView):
    model = MonthJournal
    template_name = 'journal/journal.html'

    def get_context_data(self, **kwargs):
        # get context data from TemplateView class
        context = super(JournalView, self).get_context_data(**kwargs)

        # check if we need to display some specific month
        if self.request.GET.get('month'):
            month = datetime.strptime(self.request.GET['month'], '%Y- %m - %d').date()
        else:
            # otherwise just displaying current month data
            today = datetime.today()
            month = date(today.year, today.month, 1)

        # обчислюємо поточний рік, попередній і наступний місяці
        next_month = month + relativedelta(months=1)
        prev_month = month - relativedelta(months=1)
        context['prev_month'] = prev_month.strftime('%Y -%m -%d')
        context['next_month'] = next_month.strftime('%Y -%m -%d')
        context['year'] = month.year
        context['month_verbose'] = month.strftime('%B')

        # we’ll use this variable in students pagination
        context['cur_month'] = month.strftime('%Y -%m -%d')

        # prepare variable for template to generate
        # journal table header elements
        myear, mmonth = month.year, month.month
        number_of_days = monthrange(myear, mmonth)[1]
        context['month_header'] = [{'day': d, 'verbose': day_abbr[weekday(myear, mmonth, d)][:2]}

                                   for d in range(1, number_of_days + 1)]

        # витягуємо усіх студентів посортованих по
        queryset = Student.objects.order_by('last_name')

        # це адреса для посту AJAX запиту, як бачите, ми
        # робитимемо його на цю ж в’юшку; в’юшка журналу
        # буде і показувати журнал і обслуговувати запити
        # типу пост на оновлення журналу;
        # url to update student presence, for form post
        update_url = reverse('journal')

        # пробігаємось по усіх студентах і збираємо
        # необхідні дані:

        students = []
        for student in queryset:
            # try to get journal object by month selected
            # month and current student
            try:
                journal = MonthJournal.objects.get(student=student, date=month)
            except Exception:
                journal = None

            # fill in days presence list for current student
            days = []
            for day in range(1, number_of_days + 1):
                days.append({'day': day,
                             'present': journal and getattr(journal, 'present_day % d' % day, False) or False,
                             'date': date(myear, mmonth, day).strftime('%Y -%m -%d')})

            # prepare metadata for current student
            students.append({
                'fullname': u' %s %s' % (student.last_name, student.first_name),
                'days': days,
                'id': student.id,
                'update_url': update_url, })

            # apply pagination, 10 students per page
            context = paginate(students, 10, self.request, context,
                               var_name='students')
            # finally return updated context
            # with paginated students
            return context


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