# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from .models import Hotel
from .forms import HotelForm
from django.db.models import Min, Max
from django.db.models import QuerySet
from django.shortcuts import render

# Create your views here.

class MainView(ListView, FormMixin):
    model = Hotel
    template_name = "index.html"
    form_class = HotelForm

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        is_location = request.GET.get('location', False)
        is_standard = request.GET.get('standard', False)
        if is_location:
            city = request.GET['location']
            objects = Hotel.objects.filter(location=city)
        elif is_standard:
            standard = request.GET['standard']
            if objects:
                objects = objects.filter(standard=dict(Hotel.CLASSES_CHOICES)[standard])
            else:
                objects = Hotel.objects.filter(standard=dict(Hotel.CLASSES_CHOICES)[standard])
        else:
            objects = Hotel.objects.all()
        self.object_list = objects
        context = self.get_context_data()
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        hotels = context['object_list']
        hotels = hotels.annotate(min_prize = Min('room__prize'))
        hotels = hotels.annotate(max_prize = Max('room__prize'))
        context['object_list'] = hotels
        return context