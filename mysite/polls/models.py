from __future__ import unicode_literals
from django.db import models

#Creates Households table with lat,lon,total_inc,count as columns of the table.
class Households(models.Model):
	lat = models.DecimalField(max_digits=20,decimal_places=10)
	lon = models.DecimalField(max_digits=20,decimal_places=10)
	total_inc = models.IntegerField(default=0)
	count = models.IntegerField(default=0)
	def __unicode__(self):
		return '%s'%(self.id)

#Creates Person table with house_id,name,age,gender,numb_fam as columns of the table.
class Person(models.Model):
	house_id = models.ForeignKey(Households, on_delete=models.CASCADE)
	name = models.CharField(max_length=200)
	age = models.IntegerField(default=0)
	gender = models.CharField(max_length=200)
	numb_fam = models.IntegerField(default=0)
	def __unicode__(self):
		return '%s %s'%(self.house_id,self.name)

#Creates sequence table with house_id,farm_id,seq_id,lat,lon as columns of the table.
class sequence(models.Model):
	house_id = models.ForeignKey(Households, on_delete=models.CASCADE)
	farm_id = models.IntegerField(default=0)
	seq_id = models.IntegerField(default=0)
	lat = models.DecimalField(max_digits=20,decimal_places=10)
	lon = models.DecimalField(max_digits=20,decimal_places=10)
	def __unicode__(self):
		return '%s %s'%(self.farm_id,self.seq_id)

#Creates area table with farm_id,total_area as columns of the table.
class area(models.Model):
	farm_id = models.ForeignKey(sequence, on_delete=models.CASCADE) 
	total_area = models.IntegerField(default=0)
	def __unicode__(self):
		return '%s %s'%(self.farm_id,self.total_area)

#Creates crops table with farm_id,crop_id,crop_area as columns of the table.
class crops(models.Model):
	farm_id = models.ForeignKey(sequence, on_delete=models.CASCADE)
	crop_id = models.IntegerField(default=0)
	crop_area =models.IntegerField(default=0)
	def __unicode__(self):
		return '%s %s'%(self.farm_id,self.crop_id)

#Creates wells table with farm_id,lat,lon,depth,avg_yeild as columns of the table.
class wells(models.Model):
	farm_id = models.ForeignKey(sequence, on_delete=models.CASCADE)
	lat = models.DecimalField(max_digits=20,decimal_places=10)
	lon = models.DecimalField(max_digits=20,decimal_places=10)
	depth = models.IntegerField(default=0)
	avg_yield = models.IntegerField(default=0)
	def __unicode__(self):
		return '%s %s'%(self.farm_id,self.depth)

#Creates wateryield table with farm_id,date,time,water_yeild as columns of the table.
class wateryield(models.Model):
	farm_id = models.ForeignKey(sequence, on_delete=models.CASCADE)
	date = models.DateField(max_length=200)
	time = models.TimeField(blank=True, null=True)
	water_yield = models.IntegerField(default=0)
	def __unicode__(self):
		return '%s %s'%(self.farm_id,self.water_yield)
