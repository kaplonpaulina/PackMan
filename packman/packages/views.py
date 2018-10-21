# from django.shortcuts import render
# from django.views.generic import TemplateView

# class blablaSearch(TemplateView):
# 	template_name="packages/blabla.html"
# # Create your views here.

from django.shortcuts import render
from packages.models import Package
from blablacarapi import BlaBlaCarApi
from .forms import blablaForm

from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.


# def packages_listed(request):
#     packages_list = Package.objects.order_by('sender_id')
#     package_dict = {'packages_listed':packages_list}
#     return render(request, 'packages/packages.html', context=package_dict)


def blablaRespose(request):
    if request.method=='POST':
        blablaform=blablaForm(request.POST)
        from_=request.POST.get('from_')
        to=request.POST.get('to')
        date=request.POST.get('date')
        print(from_)
        print(to)
        if blablaform.is_valid():
            api = BlaBlaCarApi(api_key="6be8006f1bc24ff7bee08866ba8211dd")

# fetch trips from London to Paris
            trips = api.trips(frm=from_, to=to)
            for trip in trips.trips:

	               print("%s: %s -> %s, %s%s, id:%s" % (trip.departure_date,
                   trip.departure_place['address'],
                   trip.arrival_place['address'],
                   trip.price['value'],trip.price['currency'],
                   trip.permanent_id))
            # return HttpResponseRedirect
    else:
        blablaform=blablaForm()
    return render(request,'test.html', {'bla':blablaform})
