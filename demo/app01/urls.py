from django.urls import  path
from .views import *
urlpatterns = [
    path("index/",index),
    path("addperson/",addperson),
    path("getperson/",getperson),
    path("deleteperson/",deleteperson),
    path("updateperson/",updateperson),
    path('addonemore/', addonemore),
    path('getonemore/', getonemore),
]