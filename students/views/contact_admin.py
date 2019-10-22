# _*_ coding: utf-8 _*_
from django.shortcuts import render, redirect
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from studentsdb.settings import ADMIN_EMAIL

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.views.generic.edit import FormView

class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allow us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form_horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        #self.helper.field_class = 'col-sm-10'

        # form button
        self.helper.add_input(Submit('send_button', _("Send")))


    from_email = forms.EmailField(
        label=_("Your email"))

    subject = forms.CharField(
        label=_("Subject"),
        max_length=128)

    message = forms.CharField(
        label=_("Message"),
        max_length=2500,
        widget=forms.Textarea)


def contact_admin(request):
    # check if form was posted
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = ContactForm(request.POST)

        # check whether user data is valid:
        if form.is_valid():
            # send email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = _("There was an error sending the letter, try to use this form later")
            else:
                message = _("The letter is sending successful")
        # redirect to some contact page with success message
        return HttpResponseRedirect(
            u'%s?status_message=%s' % (reverse('contact_admin'), message))
    # if there was not POST render blank form
    else:
        form = ContactForm()

    return render(request, 'contact_admin/form.html', {'form': form})
