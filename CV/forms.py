from django import forms
from django.utils import timezone

from .models import PersonalDetails, CV_Entry, Education


class PersonalDetailsForm(forms.ModelForm):
    contactNumber = forms.RegexField(regex=r'^\+?1?\d{9,15}$')

    class Meta:
        model = PersonalDetails

        fields = ('name', 'dob', 'contactNumber')


class CV_EntryForm(forms.ModelForm):
    class Meta:
        model = CV_Entry
        fields = ('title', 'text', 'dateStart', 'dateEnd')


class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ('facility', 'grades', 'dateStart', 'dateEnd')
