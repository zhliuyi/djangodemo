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
    path('updateonemore/', updateonemore),
    path('deleteonemore/', deleteonemore),
    path('manytomanyadd/', manytomanyadd),
    path('manytomanyget/', manytomanyget),
    path('manytomanyupdate/', manytomanyupdate),
    path('manytomanydelete/', manytomanydelete),
    path('jhtest/', jhtest),
    path('Ftest/', Ftest),
    path('Qtest/', Qtest),

]