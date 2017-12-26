# _*_ coding: utf-8 _*_

from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models.groups import Group

from django.views.generic import CreateView, UpdateView, DeleteView

from django.forms import ModelForm

from django.core.urlresolvers import reverse, reverse_lazy

from .. util import paginate, get_current_group

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.bootstrap import FormActions

    # Views for Groups


def groups_list(request):
    # check if we need to show only one group of students
    current_group = get_current_group(request)
    print (current_group)
    if current_group:
        groups = Group.objects.filter(id=current_group.id)
    else:
        # otherwise show all students
        groups = Group.objects.all()

    # try to order groups list

    order_by = request.GET.get('order_by', '')
    if order_by in ('title', 'leader'):
        groups = groups.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            groups = groups.reverse()

    else:
        groups = groups.order_by('title')

    # paginator groups
    context = paginate(groups, 5, request, {}, var_name='groups')

    return render(request, 'groups/groups_list.html', context)
"""
    paginator = Paginator(groups, 2)
    page = request.GET.get('page')
    try:
        groups = paginator.page(page)
    except PageNotAnInteger:
        # If page not integer, deliver first page
        groups = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        groups = paginator.page(paginator.num_pages)

    return render(request, 'groups/groups_list.html', {'groups': groups})
    """

class GroupAddForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'leader', 'notes']

    def __init__(self, *args, **kwargs):
        super(GroupAddForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('groups_add')
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


class GroupAddView(SuccessMessageMixin, CreateView):
    model = Group
    template_name = 'groups/groups_add.html'
    form_class = GroupAddForm
    success_url = '/groups'
    success_message = u"Група %(title)s успішно створена"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, title=self.object.title)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(request, messages.INFO, u'Створення групи відмінено')
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(GroupAddView, self).post(request, *args, **kwargs)


class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'leader', 'notes']

    def __init__(self, *args, **kwargs):
        super(GroupUpdateForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_action = reverse('groups_edit',
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


class GroupUpdateView(SuccessMessageMixin, UpdateView):
    model = Group
    template_name = 'groups/groups_add.html'
    form_class = GroupUpdateForm
    success_url = '/groups'
    success_message = u"Група %(title)s успішно змінена"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(cleaned_data, title=self.object.title)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(request, messages.INFO, u'Редагувння групи відмінено')
            return HttpResponseRedirect(reverse('groups'))
        else:
            return super(GroupUpdateView, self).post(request, *args, **kwargs)


class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'groups/groups_delete.html'
    form_class = GroupUpdateForm
    success_url = reverse_lazy('groups')
    success_message = u"Група успішно видалена"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(GroupDeleteView, self).delete(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            messages.add_message(request, messages.INFO, u'Видалення групи відмінено')
            return HttpResponseRedirect(reverse('groups'))

        else:
            return super(GroupDeleteView, self).post(request, *args, **kwargs)
