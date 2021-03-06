# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def index(request):
    if 'attempt' not in request.session:
        request.session['attempt']=0
    request.session['attempt'] += 1
    context = {
        'word':get_random_string(length=14)
    }
    return render(request, "random_word/index.html", context)
def reset(request):
    request.session['attempt']=0
    return redirect('/random_word')