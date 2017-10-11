# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Person,Households,area,sequence,crops,wells,wateryield

# Register your models here.
admin.site.register(Person)
admin.site.register(Households)
admin.site.register(area)
admin.site.register(sequence)
admin.site.register(crops)
admin.site.register(wells)
admin.site.register(wateryield)

# Register your models here.
