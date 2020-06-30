from django.shortcuts import render, redirect


def home_page(request):
    return render(request, 'home.html')


def blog(request):
    return redirect('blog')
