# coding: utf-8
from datetime import time
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.conf import settings
from eventex.core.models import Speaker, Talk

def homepage(request):
    context = {'STATIC_URL': settings.STATIC_URL}
    return render(request, 'index.html')

def speaker_detail(request, slug):
    speaker = get_object_or_404(Speaker, slug=slug)
    context = {'speaker': speaker}
    return render(request, 'core/speaker_detail.html', context)

def talk_list(request):
    from django.http import HttpResponse
    return HttpResponse()

def talk_list(request):
    return render(request, 'core/talk_list.html')

def talk_list(request):
    midday = time(12)
    context = {
        'morning_talks': Talk.objects.filter(start_time__lt=midday),
        'afternoon_talks': Talk.objects.filter(start_time__gte=midday),
    }
    return render(request, 'core/talk_list.html', context)