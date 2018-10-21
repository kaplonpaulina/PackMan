from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import render



# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

app_name = 'packages'

urlpatterns = [
    # url(r'^pack$',views.packages_listed,name='packages'),
    url(r'^test/$',views.blablaRespose,name='packages'),
]