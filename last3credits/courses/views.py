# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Course

sis_apikey = "VltZPiXbs4bnJlr886paVA9MtEn5ornC"
# Create your views here.
def index(request):
    course_list = Course.objects.order_by('-code')
    template = loader.get_template('courses/index.html')
    context = {
        'course_list': course_list,
    }
    return render(request, 'courses/index.html', {'course_list': course_list})

def detail(request, code):
    course = get_object_or_404(Course, pk=code)
    return render(request, 'courses/detail.html', {'course': course})
