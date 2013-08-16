# coding: utf-8
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.conf import settings
from eventex.core.models import Speaker

def homepage(request):
	context = {'STATIC_URL': settings.STATIC_URL}
	return render(request, 'index.html')

def speaker_detail(request, slug):
	speaker = get_object_or_404(Speaker, slug=slug)
	context = {'speaker': speaker}
	return render(request, 'core/speaker_detail.html', context)