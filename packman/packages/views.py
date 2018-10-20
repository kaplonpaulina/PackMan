from django.shortcuts import render
from packages.models import Package

# Create your views here.


def packages_listed(request):
    packages_list = Package.objects.order_by('sender_id')
    package_dict = {'packages_listed':packages_list}
    return render(request, 'packages/packages.html', context=package_dict)
