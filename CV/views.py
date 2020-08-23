from django.shortcuts import render, redirect, get_object_or_404

from CV.forms import PersonalDetailsForm, CV_EntryForm, EducationForm
from CV.models import CV_Entry, PersonalDetails, Education


def home_page(request):
    entries = CV_Entry.objects.all()
    pd = PersonalDetails.objects.first()
    education = Education.objects.all()
    return render(request, 'home.html', {'cv_entries': entries, 'personaldetails': pd, 'education': education})


def personDet_edit(request):
    personalDetails = PersonalDetails.objects.first();
    if request.method == "POST":
        form = PersonalDetailsForm(request.POST, instance=personalDetails)
        if form.is_valid():
            personalDetails = form.save()
            personalDetails.author = request.user
            personalDetails.save()
            return redirect('/')
    else:
        form = PersonalDetailsForm(instance=personalDetails)
    return render(request, 'blog/post_edit.html', {'form': form, 'name' : 'Personal Details'})


def blog(request):
    return redirect('blog')


def newCV(request):
    if request.method == "POST":
        form = CV_EntryForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
        return redirect('/')
    else:
        form = CV_EntryForm
    return render(request, 'blog/post_edit.html', {'form': form, 'name' : 'New CV Entry'})


def CV_Entry_edit(request, pk):
    post = get_object_or_404(CV_Entry, pk=pk)
    if request.method == "POST":
        form = CV_EntryForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = CV_EntryForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'name' : 'Edit CV Entry'})


def CV_Entry_remove(request, pk):
    post = get_object_or_404(CV_Entry, pk=pk)
    post.delete()
    return redirect('/')


def Education_new(request):
    if request.method == "POST":
        form = EducationForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = EducationForm
    return render(request, 'blog/post_edit.html', {'form': form, 'name' : 'New Education'})


def Education_edit(request, pk):
    post = get_object_or_404(Education, pk=pk)
    if request.method == "POST":
        form = EducationForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = EducationForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'name' : 'Edit Education'})


def Education_remove(request, pk):
    post = get_object_or_404(Education, pk=pk)
    post.delete()
    return redirect('/')
