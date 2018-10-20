from django.shortcuts import render
from django.http import HttpResponse
from packages.models import Package

# Create your views here.

def index(request):
    webpages_list = Package.objects.order_by('senderId')
    senderId_dict = {'package':webpages_list}
    return render(request, 'pakcges/index.html',context=senderId_dict)
