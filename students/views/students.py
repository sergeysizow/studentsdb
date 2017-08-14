# _*_ coding: utf-8 _*_
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.core.urlresolvers import reverse, reverse_lazy

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from datetime import datetime

from PIL import Image

from ..models.students import Student

from ..models.groups import Group

from django.views.generic import CreateView, UpdateView, DeleteView

from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions


# Views for Students

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

def students_add(request):
    # was form posted?
    if request.method == "POST":
        # was form are button clicked?
        if request.POST.get('add_button') is not None:

            # errors collection
            errors = {}

            # validate student data will go here
            data = {'middle_name': request.POST.get('middle_name'), 'notes': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Ім'я є обов'язковим для заповнення"
            else:
                data['first_name'] = first_name

            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = u"Прізвище є обов'язковим для заповнення"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = u"Дата народження є обов'язковою"
            else:
                data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()
            if not ticket:
                errors['ticket'] = u"Квиток є обов'язковим"
            else:
                try:
                    datetime.strptime(birthday, '%Y-%m-%d')
                except Exception:
                    errors['birthday'] = u"Ведіть коректний формат дати (наприклад 1989-08-24)"
                else:
                    data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = u"Оберіть групу для студента"
            else:
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = u"Оберіть коректну групу"
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            try:
                img = Image.open(photo, 'r')

                if photo.size <= 2097152:
                    data['photo'] = photo
                else:
                    errors['photo'] = u"Оберіть фото менше 2Mb"

            except:
                errors['photo'] = u"Оберіть фото"

            # save student to database
            if not errors:
                student = Student(**data)
                student.save()

                # redirect user to students_list
                return HttpResponseRedirect(
                    u'{}?status_message=Студента {} {} успішно додано!'.format(reverse('home'), first_name, last_name)
                    )

            else:
                # render form with errors and previous user input
                return render(request, 'students/students_add.html',
                              {'groups': Group.objects.all().order_by('title'), 'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(
                u'%s?status_message=Додавання студента скасовано!' %
                reverse('home'))
    else:
        # initial form render
        return render(request, 'students/students_add.html',
                      {'groups': Group.objects.all().order_by('title')})

"""

class StudentAddForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'birthday', 'photo', 'ticket', 'student_group', 'notes']


    def __init__(self, *args, **kwargs):
        super(StudentAddForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('students_add')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control_label'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout.append(FormActions(
            Submit('add_button', u'Зберегти', css_class='btn btn-primary'),
            Submit('cancel_button', u'Скасувати', css_class='btn btn-link'),
        ))


class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'birthday', 'photo', 'ticket', 'student_group', 'notes']

    def __init__(self, *args, **kwargs):
        super(StudentUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('students_edit',
                                          kwargs={'pk': kwargs['instance'].id})
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control_label'
        self.helper.field_class = 'col-sm-10'

        self.helper.layout.append(FormActions(
            Submit('add_button', u'Зберегти', css_class='btn btn-primary'),
            Submit('cancel_button', u'Скасувати', css_class='btn btn-link'),
        ))


class StudentAddView(SuccessMessageMixin, CreateView):
    model = Student
    template_name = 'students/students_add.html'
    form_class = StudentAddForm
    success_url = '/'
    success_message = u"Студент %(last_name)s успішно створений"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, last_name=self.object.last_name)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(request, messages.INFO, u'Створення студента відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentAddView, self).post(request, *args, **kwargs)


class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    template_name = 'students/students_edit.html'
    form_class = StudentUpdateForm
    success_url = '/'
    success_message = u"Студент %(last_name)s успішно редактований"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, last_name=self.object.last_name)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(request, messages.INFO, u'Редагування студента відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(StudentUpdateView, self).post(request, *args, **kwargs)


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'
    form_class = StudentUpdateForm
    success_url = reverse_lazy('home')
    success_message = u"Студента успішно видалено"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(StudentDeleteView, self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(request, messages.INFO, u'Видалення студента відмінено')
            return HttpResponseRedirect(reverse('home'))

        else:
            return super(StudentDeleteView, self).post(request, *args, **kwargs)