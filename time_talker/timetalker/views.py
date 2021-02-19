import os
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from time_talker.settings import BASE_DIR
from django.shortcuts import render

file_path = os.path.join(BASE_DIR, 'front\cu.html')


def index(request):
    context = {}
    return render(request, 'timetalker/cu.html', context)
