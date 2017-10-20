from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^newInterest$', views.new),
    url(r'^addInterest$', views.add),
    url(r'^(?P<interest_id>\d+)/delete$', views.delete),
]
