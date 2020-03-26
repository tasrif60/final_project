
from django import forms
from django.forms import Textarea

from .models import Schedule, Profile


class ScheduleForm(forms.ModelForm):
    all_data = Profile.objects.filter()


    class Meta:
        model = Schedule
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['employee'].empty_label = 'Select'
