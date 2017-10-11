# -*- coding: utf-8 -*-
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

@csrf_exempt
def send_table_data(request,name):
	if request.method=='GET':	
		if name=='households':
			Household = Households.objects.all()
			serializer = Households_serializer(Household, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='person':
			persons = Person.objects.all()
			serializer = Person_serializer(persons, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='sequence':
			sequences = sequence.objects.all()
			serializer = sequence_serializer(sequences, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='area':
			Area = area.objects.all()
			serializer = area_serializer(Area, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='crops':
			crop = crops.objects.all()
			serializer = crops_serializer(crop, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='wells':
			well = wells.objects.all()
			serializer = wells_serializer(well, many=True)
			return JsonResponse(serializer.data, safe=False)
		if name=='wateryield':
			yields = wateryield.objects.all()
			serializer = wateryield_serializer(yields, many=True)
			return JsonResponse(serializer.data, safe=False)



