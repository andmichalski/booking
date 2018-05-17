# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView
from .models import Hotel
from django.db.models import QuerySet
from django.shortcuts import render

# Create your views here.

class MainView(ListView):
    model = Hotel
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        if 'location' in request.GET:
            city = request.GET['location']
            self.object_list = Hotel.objects.filter(location=city)
        if 'standard' in request.GET:
            standard = request.GET['location']
            self.object_list = Hotel.objects.filter(standard=standard)
        context = self.get_context_data()
        return self.render_to_response(context)
