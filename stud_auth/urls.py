from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^login$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout$', views.logout_view, name='logout'),
    url(r'^register$', views.RegisterFormView.as_view(), name='register'),
    url(r'^email_validate', views.email_validate, name='email_validate'),
    url(r'^profile/(?P<pk>\d+)/edit/$', views.ProfileEdit.as_view(), name='profile_edit'),
    url(r'^profile', TemplateView.as_view(template_name='profile.html'), name='profile'),
    url(r'^users/$', views.UsersList.as_view(), name='users'),
    url(r'^password/(?P<pk>\d+)/change/$', views.ChangePassword.as_view(), name='change_password'),
    ]
