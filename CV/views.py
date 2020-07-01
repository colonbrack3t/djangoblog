from django.shortcuts import render, redirect

from CV.models import CV_Entry, PersonalDetails


def home_page(request):
    entries = CV_Entry.objects.all()
    pd = PersonalDetails.objects.first()
    return render(request, 'home.html', {'cv_entries': entries, 'personaldetails': pd})


def blog(request):
    return redirect('blog')
