from django.conf.urls import url

from . import views

urlpatterns = [
     url(r'^polls/(?P<name>[a-z]+)/$', views.send_table_data),
]

