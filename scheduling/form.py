from django import forms
from .models import Schedule, Profile


class ScheduleForm(forms.ModelForm):
    title = forms.CharField(max_length=100, )
    employee = forms.ChoiceField()
    start_time = forms.CharField(max_length=50)
    end_time = forms.CharField(max_length=50)
    note = forms.CharField(max_length=200)

    class Meta:
        model = Schedule
        fields = '__all__'
