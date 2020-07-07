from django.conf.urls import url

from sellysafeweb import views

app_name = 'sellysafeweb'

urlpatterns = [
    url(r'about', views.about, name='about'),
    url(r'map', views.map, name='map'),
]
