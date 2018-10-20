from django.contrib.auth import login, logout
from django.urls import reverse_lazy
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from accounts.models import User
from django.shortcuts import render

from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


def users_listed(request):
    users_list = User.objects.order_by('first_name')
    user_dict = {'users_listed':users_list}
    return render(request, 'accounts/users.html', context=user_dict)
