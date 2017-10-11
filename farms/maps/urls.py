from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^maps/index/$', views.index),#Whenever the mentioned url is opened it will access its respected functions in views
	url(r'^maps/house/$',views.house),#Whenever the mentioned url is opened it will access its respected functions in views
	url(r'^maps/wel/$',views.wel),#Whenever the mentioned url is opened it will access its respected functions in views
]
