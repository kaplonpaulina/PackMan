from django.contrib.auth import login, logout
from django.urls import reverse_lazy
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core.mail import send_mail

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
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
    username=request.user.username
    email=request.user.email
    subject, from_email, to = 'Subject', 'pacman.package.sender@gmail.com', ['maria.anna.mamica@gmail.com','kartytko@gmail.com']
    html_content = render_to_string('accounts/temp.html', {'user':username,'email':email}) # render with dynamic value
    text_content = strip_tags(html_content) # Strip the html tag. So people can see the pure text at least.

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    return HttpResponse("return this string")