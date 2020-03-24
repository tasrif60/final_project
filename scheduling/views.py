from django.shortcuts import render
from .models import Schedule
from .form import ScheduleForm


def details(request, *args, **kwargs):
    allschedule = Schedule.objects.all()
    allList = {

        'object': allschedule

    }
    return render(request, 'schedule_list.html', allList)


def create_schedule(request, *args, **kwargs):

    if request.method == 'POST':
        sch_form = ScheduleForm(request.POST)
        if sch_form.is_valid():
            sch_form.save(commit=True)
    form = ScheduleForm()
    return render(request, 'create_schedule.html', {'form': form})


def show_calender(request, *args, **kwargs):
    return render(request, 'calendar.html')
