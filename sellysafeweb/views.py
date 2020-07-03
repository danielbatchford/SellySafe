from django.shortcuts import render

from SellySafe import settings
from sellysafeweb.forms import ReportForm
from sellysafeweb.models import Report


def map(request):
    form = ReportForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return render(request, 'sellysafeweb/confirmation.html')

    reports = Report.objects.all()
    return render(request, 'sellysafeweb/map.html', {
        'reports': reports,
        'form': ReportForm(),
        'map_box_key': settings.MAPBOX_KEY,
        'city_center': settings.CITY_CENTER,
        'bounds': settings.BOUNDS})
