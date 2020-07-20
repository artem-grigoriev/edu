import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, Http404
def index(request):
    return render(request, 'mainpage/index.html')
def feedback(request):
    return render(request, 'mainpage/feedback.html')
def news(request):
    return render(request, 'mainpage/news.html')
def contact(request):
    return render(request, 'mainpage/contact.html')