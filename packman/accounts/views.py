from django.contrib.auth import login, logout
from django.urls import reverse_lazy
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import send_mail


from . import forms
from . import models


from django.contrib.auth import get_user_model
User = get_user_model()

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


@csrf_exempt
def send(request):
    message=request.user.username + request.user.
    print(message)
    send_mail(
    'kupa',
    message,
    'pacman.package.sender@gmail.com',
    ['kartytko@gmail.com','elakrz@gmail.com','kaplonpaulina97@gmail.com','maria.anna.mamica@gmail.com'],)
    return HttpResponse("return this string")

