from django.http import HttpResponse
import json
import requests
from django.shortcuts import render
def index(request):
	return render(request, 'maps/index.html')#returns the requested html page

def house(request):
	r=requests.get('http://127.0.0.1:8081/polls/households/')#Retrieves data from the mentioned server link
	j = r.json()
	house_lat=[]
	house_lon=[]
	house_id=[]
	house_inc=[]
	house_count=[]
	for i in xrange(len(j)):
		house_lat.append(float(j[i]['lat']))
		house_lon.append(float(j[i]['lon']))
		house_id.append(j[i]['id'])
		house_inc.append(int(j[i]['total_inc']))
		house_count.append(j[i]['count'])
		#Loading the data received from server into the above variables
	context= {'house_lat':house_lat,'house_lon':house_lon,'house_id':house_id,'house_inc':house_inc,'house_count':house_count}
	return render(request,'maps/house.html',context)#To access the variables in the mentioned link

def wel(request):
	r = requests.get('http://127.0.0.1:8081/polls/sequence/')#Retrieves data from the mentioned server link
	j = r.json()
	farm_lat=[]
	farm_lon=[]
	farm_id=[]
	for i in xrange(len(j)):
		farm_lat.append(float(j[i]['lat']))
		farm_lon.append(float(j[i]['lon']))
		farm_id.append(j[i]['farm_id'])
		#Loading the data received from server into the above variables
	r1=requests.get('http://127.0.0.1:8081/polls/households/')#Retrieves data from the mentioned server link
	j1 = r1.json()
	house_lat=[]
	house_lon=[]
	house_id=[]
	house_inc=[]
	for i in xrange(len(j1)):
		house_lat.append(float(j1[i]['lat']))
		house_lon.append(float(j1[i]['lon']))
		house_id.append(j1[i]['id'])
		house_inc.append(j1[i]['total_inc'])
		#Loading the data received from server into the above variables
	r2=requests.get('http://127.0.0.1:8081/polls/wells/')#Retrieves data from the mentioned server link
	j2 = r2.json()
	well_lat=[]
	well_lon=[]
	well_id=[]
	well_farm_id=[]
	well_depth=[]
	well_avg_yeild=[]
	for i in xrange(len(j2)):
		well_lat.append(float(j2[i]['lat']))
		well_lon.append(float(j2[i]['lon']))
		well_id.append(j2[i]['id'])
		well_farm_id.append(j2[i]['farm_id'])
		well_depth.append(j2[i]['depth'])
		well_avg_yeild.append(j2[i]['avg_yield'])
		#Loading the data received from server into the above variables
	context={'farm_lat':farm_lat,'farm_lon':farm_lon,'farm_id':farm_id,'house_lat':house_lat,'house_lon':house_lon,'house_id':house_id,'house_inc':house_inc,'well_lat':well_lat,'well_lon':well_lon,'well_id':well_id,'well_farm_id':well_farm_id,'well_depth':well_depth,'well_avg_yeild':well_avg_yeild}
	return render(request,'maps/wel.html',context)#To access the variables in the mentioned link
	
