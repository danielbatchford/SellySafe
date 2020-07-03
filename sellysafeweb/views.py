from django.shortcuts import render

from SellySafe import settings


def map(request):
    return render(request, 'sellysafeweb/map.html', {'map_box_key': settings.MAP_BOX_KEY})