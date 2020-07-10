from django.conf.urls import url

from sellysafeweb import views

app_name = 'sellysafeweb'

urlpatterns = [

    # About page view
    url(r'about', views.about, name='about'),

    # Main map view
    url(r'map', views.map, name='map'),

    # Feedback Confirmation view once feedback page recieves a valid response
    url(r'feedback_confirmation', views.feedback_confirmation, name='feedback_confirmation'),

    # Page to submit feedback
    url(r'feedback', views.feedback, name='feedback'),

    # Blank URL redirect
    url('', views.redirect_to_map, name='redirect_to_map')
]
