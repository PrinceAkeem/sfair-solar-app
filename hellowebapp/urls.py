"""hellowebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from collection.backends import MyRegistrationView
from collection import views
from django.contrib.auth.views import (
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete,
)

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about/$',
        TemplateView.as_view(template_name='about.html'),
        name='about'),
    url(r'^contact/$',
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url(r'^piechart/$',
        TemplateView.as_view(template_name='piechart.html'),
        name='piechart'),   # delete this in a bit
    url(r'^powerwall/$',
        TemplateView.as_view(template_name='powerwall.html'),
        name='powerwall'),
    url(r'^pricing/$',
        TemplateView.as_view(template_name='pricing.html'),
        name='pricing'),
    url(r'^solarpanels/$',
        TemplateView.as_view(template_name='solarpanels.html'),
        name='solarpanels'),
    url(r'^profiles/(?P<slug>[-\w]+)/$', views.profile_detail,
       name='profile_detail'),
    url(r'^profiles/(?P<slug>[-\w]+)/edit/$', views.edit_profile,
       name='edit_profile'),
    url(r'^myaccount/$',
        TemplateView.as_view(template_name='myaccount.html'),
        name='myaccount'),
    url(r'^accounts/register/$', MyRegistrationView.as_view(),
            name='registration_register'),
    url(r'^accounts/create_my_solar/$',
            views.create_my_solar,
            name='registration_create_my_solar'),

    # the new browse flow
    url(r'^browse/name/$',
        views.browse_by_name, name='browse'),
    url(r'^browse/name/(?P<initial>[-\w]+)/$',
        views.browse_by_name, name='browse_by_name'),
    # the new password reset URLs
    url(r'^accounts/password/reset/$', password_reset,
        {'template_name': 'registration/password_reset_form.html'},
        name="password_reset"),
     url(r'^accounts/password/reset/done/$',
        password_reset_done,
        {'template_name': 'registration/password_reset_done.html'},
        name="password_reset_done"),

    # the below should all be on one line
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1, 13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
    url(r'^accounts/password/done/$',
        password_reset_complete,
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
]
