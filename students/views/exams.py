# _*_ coding: utf-8 _*_

from django.shortcuts import render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.http import HttpResponse, HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.exams import Exam
from django.forms import ModelForm
from django.views.generic import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse, reverse_lazy

from ..util import paginate, get_current_group

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions, AppendedText

# Views for Exams


def exams_list(request):
    # check if we need to show only one group of students
    current_group = get_current_group(request)
    if current_group:
        exams = Exam.objects.filter(student_group=current_group)
    else:
        # otherwise show all students
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

    context = paginate(exams, 3, request, {}, var_name='exams')

    return render(request, 'exams/exams_list.html', context)


class ExamAddForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'date', 'teacher', 'student_group', 'location', 'notes']

    def __init__(self, *args, **kwargs):
        super(ExamAddForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('exams')
        self.helper.form_method = 'POST'
        self.helper.form_class = 'form-horizontal'

        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control_label'
        self.helper.field_class = 'col-sm-3'

        self.helper.layout.append(FormActions(
            Submit('add_button', u'Зберегти', css_class='btn btn-primary'),
            Submit('cancel_button', u'Скасувати', css_class='btn btn-link'),
        ))

        self.helper.layout[1] = AppendedText('date',
                                             '<span class="glyphicon glyphicon-calendar"></span>', active=True)


class ExamAddView(SuccessMessageMixin, CreateView):
    model = Exam
    template_name = 'exams/exams_add.html'
    form_class = ExamAddForm
    #success_url = '/exams'
    success_message = u"Екзамен %(title)s успішно створено"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, title=self.object.title)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(request, messages.INFO, u'Створення екзамену відмінено')
            return HttpResponseRedirect(reverse('/exams'))
        else:
            return super(ExamAddView, self).post(request, *args, **kwargs)


class ExamUpdateForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'date', 'teacher', 'student_group', 'location', 'notes']

    def __init__(self, *args, **kwargs):
        super(ExamUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('exams_edit',
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


class ExamUpdateView(SuccessMessageMixin, UpdateView):
    model = Exam
    template_name = 'exams/exams_edit.html'
    form_class = ExamUpdateForm
    success_url = '/exams'
    success_message = u"Екзамен %(title)s успішно відредактовано"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, title=self.object.title)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(request, messages.INFO, u'Редагуваня екзамену відмінено')
            return HttpResponseRedirect(reverse('exams'))
        else:
            return super(ExamUpdateView, self).post(request, *args, **kwargs)


class ExamDeleteView(DeleteView):
    model = Exam
    template_name = 'exams/exams_delete.html'
    success_url = reverse_lazy('exams')
    success_message = u"Екзамен успішно видалений"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ExamDeleteView, self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(request, messages.INFO, u'Видалення екзамену відмінено')
            return HttpResponseRedirect(reverse('exams'))

        else:
            return super(ExamDeleteView, self).post(request, *args, **kwargs)
