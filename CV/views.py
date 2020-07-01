from django.shortcuts import render, redirect

from CV.models import CV_Entry


def home_page(request):
    entries = CV_Entry.objects.all()
    return render(request, 'home.html', {'cv_entries': entries})


def blog(request):
    return redirect('blog')
