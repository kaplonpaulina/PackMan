from django.contrib import auth
from django.db import models
from django.utils import timezone


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('accounts.views.details', args=[str(self.id)])
