from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name = 'packages'

urlpatterns = [
    url(r'^$',views.packages_listed,name='packages'),
]
