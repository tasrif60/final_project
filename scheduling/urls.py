from django.urls import path
from scheduling.views import create_schedule, details,show_calender

urlpatterns = [

    path('schedule_list.html', details),
    path('create_schedule.html', create_schedule),
    path('calendar.html', show_calender),


]