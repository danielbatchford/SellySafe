from django.conf.urls import url

from sellysafeweb import views

app_name = 'sellysafeweb'

urlpatterns = [
    url(r'about', views.about, name='about'),
    url(r'map', views.map, name='map'),
    url(r'feedback_confirmation', views.feedback_confirmation, name='feedback_confirmation'),
    url(r'feedback', views.feedback, name='feedback'),
    url('', views.redirect_to_map, name='redirect_to_map')
]
