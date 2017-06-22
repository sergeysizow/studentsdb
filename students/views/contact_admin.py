# _*_ coding: utf-8 _*_
from django.shortcuts import render, redirect
from django import forms
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from studentsdb.settings import ADMIN_EMAIL

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from django.views.generic.edit import FormView

class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        #call original initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        #this helper object allow us to customize form
        self.helper = FormHelper()

        #form tag attributes
        self.helper.form_class = 'form_horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        #twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        #form button
        self.helper.add_input(Submit('send_button', u'Надіслати'))

    from_email = forms.EmailField(
        label=u"Ваша емейл адреса")

    subject = forms.CharField(
        label=u"Заголовок листа",
        max_length=128)

    message = forms.CharField(
        label=u"Текст повідомлення",
        max_length=2500,
        widget=forms.Textarea)


def contact_admin(request):
    #check if form was posted
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = ContactForm(request.POST)

        #check whether user data is valid:
        if form.is_valid():
            #send email
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            from_email = form.cleaned_data['from_email']

            try:
                send_mail(subject, message, from_email, [ADMIN_EMAIL])
            except Exception:
                message = u'Під час відправки листа сталась помилка, спробуйте скористатись даною формою пізніше'
            else:
                message = u'Повідомлення успішно відправлено'
        #redirect to some contact page with success message
        return HttpResponseRedirect(
            u'%s?status_message=%s' % (reverse('contact_admin'), message))
    #if there was not POST render blank form
    else:
        form = ContactForm()

    return render(request, 'contact_admin/form.html', {'form': form})

"""

class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].label = u"Тема"
        self.fields['from_email'].label = "Your email:"
        self.fields['message'].label = "What do you want to say?"



class ContactView (FormView):
    template_name = 'contact_admin/form.html'
    form_class = ContactForm
    success_url = '/email-sent'


    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        from_email = form.cleaned_data['from_email']

        send_mail(subject, message, from_email, [ADMIN_EMAIL])

        return super(ContactView, self).form_valid(form)

"""