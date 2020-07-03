from django.conf.urls import url
from django.urls import path

from sellysafeweb import views

app_name = 'sellysafeweb'

urlpatterns = [
    url(r'',views.map, name = 'map')
]