# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from hotels.models import Hotel, Room

from django.contrib import admin

# Register your models here.

admin.site.register(Hotel)
admin.site.register(Room)
