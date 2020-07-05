from django.shortcuts import render, redirect
import datetime as dt

from django.utils.timezone import make_aware
from django.utils import timezone
from SellySafe import settings
from sellysafeweb.forms import ReportForm
from sellysafeweb.models import Report


def map(request):

    show_modal = True

    form = ReportForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            report = Report.objects.create(contents=form.cleaned_data['contents'],
                                           lat=form.cleaned_data['lat'],
                                           long=form.cleaned_data['long'],
                                           datetime=form.cleaned_data['datetime'])
            report.save()
            return redirect('sellysafeweb:map')

    cutoff_date = dt.date.today() - dt.timedelta(days = settings.SHOW_DURATION)
    reports = Report.objects.filter(datetime__gte=cutoff_date)

    return render(request, 'sellysafeweb/map.html', {
        'reports': reports,
        'form': form,
        'map_box_key': settings.MAPBOX_KEY,
        'city_center': settings.CITY_CENTER,
        'bounds': settings.BOUNDS,
        'duration': settings.SHOW_DURATION,
    })


def about(request):
    return render(request, 'sellysafeweb/about.html')


def confirmation(request):
    return render(request, 'sellysafeweb/confirmation.html')
