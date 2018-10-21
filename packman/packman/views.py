from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from packages.models import Package
from django.shortcuts import render

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("test"))
        return super().get(request, *args, **kwargs)

class SenderPage(TemplateView):
    template_name = 'sender.html'

    def get(self, request, *args, **kwargs):
        if request.GET.get('user'):
            try:
                message = 'You submitted: %r' % request.GET['user']
                user = User.objects.get(id=request.GET['user'])
                user_dict = {'sender':user}
                return render(request, 'sender.html', context=user_dict)
                # user_id = int(request.POST['id'])
                # user = User.objects.get(id=user_id)
            except ValueError:
                no_sender = "Ups..."
                user_dict = {'no_sender':no_sender}
                return render(request, 'sender.html', context=user_dict)
        else:
            message = 'You submitted nothing!'
        print(message)
        return super().get(request, *args, **kwargs)

class ProfilePage(TemplateView):
    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):

        packages_list = Package.objects.order_by('-date_start_of_delivery')
        user_dict = {'profile_packages':packages_list}
        return render(request, 'profile.html', context=user_dict)
