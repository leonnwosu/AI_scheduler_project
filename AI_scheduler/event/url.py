from django.urls import path
from .views import *



urlpatterns = [
    path('makeevent',add_event,name='add_event'),
    path('<int:pk>/events', get_events, name = 'get_events'),
    path('<int:uk>/events/<int:pk>', get_one_event, name='get_one_event')
]