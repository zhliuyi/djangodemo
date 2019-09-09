"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.about),#因为路由匹配规则是从上到下，所以输入index，显示about页面的内容
    path('index/', views.index),
    path('about/', views.about),
    re_path(r'^$',views.index),#这个是当输入http://127.0.0.1:8000/，后面为空，就不会再报错而是转向index页面
    re_path(r'urltest/(\d)',views.urltest),#这样可以传值
    re_path(r'urltestnew/(?P<year>\d{4})/(?P<city>\w+)', views.urltestnew),#这里使用正则表达式，语句相当于year=\d{4}...,给固定了，所以在传给页面的时候值就不会乱

    path('gethtml/',views.gethtml),
    path('indextmp/',views.indextmp),
    path('abc/',views.abc),
    re_path('tpltest/(\d+)',views.tpltest),
    path("statictest/",views.statictest),
    path("staticdemo/",views.staticdemo),
    path("staticdemo2/",views.staticdemo2)
]
