from django.urls import path
from .views import *

urlpatterns = [
    path('addschedule', create_schedule, name='create_schedule'),
    path('schedules',get_all_schedules, name='get_all_schedules' ),
    path('schedules/<str:pk>',get_schedule,name ='get_schedule' ),
    path('schedules/<str:pk>/delete',delete_schedule,name='delete_schedule')

]