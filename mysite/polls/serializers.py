from rest_framework import serializers

from .models import *

#Households database table can be displayed in json format using serializer 
class Households_serializer(serializers.ModelSerializer):
    class Meta:
        model=Households
        fields=('id','lat','lon','total_inc','count')

#Person database table can be displayed in json format using serializer
class Person_serializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=('id','house_id','name','gender','age','numb_fam')

#sequence database table can be displayed in json format using serializer
class sequence_serializer(serializers.ModelSerializer):
    class Meta:
        model=sequence
        fields=('id','house_id','farm_id','seq_id','lat','lon')

#area database table can be displayed in json format using serializer
class area_serializer(serializers.ModelSerializer):
    class Meta:
        model=area
        fields=('id','farm_id','total_area')

#crops database table can be displayed in json format using serializer
class crops_serializer(serializers.ModelSerializer):
    class Meta:
        model=crops
        fields=('id','farm_id','crop_id','crop_area')

#wells database table can be displayed in json format using serializer
class wells_serializer(serializers.ModelSerializer):
    class Meta:
        model=wells
        fields=('id','farm_id','lat','lon','depth','avg_yield')

#wateryield database table can be displayed in json format using serializer
class wateryield_serializer(serializers.ModelSerializer):
    class Meta:
        model=wateryield
        fields=('id','farm_id','date','time','water_yield')
