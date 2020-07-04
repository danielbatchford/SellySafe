from django.shortcuts import render, redirect

from SellySafe import settings
from sellysafeweb.forms import ReportForm
from sellysafeweb.models import Report


def map(request):
    form = ReportForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('sellysafeweb:map')

    reports = Report.objects.all()
    return render(request, 'sellysafeweb/map.html', {
        'reports': reports,
        'form': form,
        'map_box_key': settings.MAPBOX_KEY,
        'city_center': settings.CITY_CENTER,
        'bounds': settings.BOUNDS
    })


def about(request):
    return render(request, 'sellysafeweb/about.html')


def confirmation(request):
    return render(request, 'sellysafeweb/confirmation.html')
