from django.urls import path
from django.contrib import admin
from.import views

urlpatterns=[
    
    path('',views.index,name="index"),
    path('index/',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('fruit/',views.fruit,name="fruit"),
    path('login/',views.login,name="login"),
    path('home/',views.home,name="home"),
    path('log/',views.log,name="log"),
    path('register/',views.register,name="register"),
    path('upload/',views.log,name="upload"),
    path('file/',views.file,name="file"),
    path('fileresult/',views.fileresult,name="fileresult"),
    path('imageCaputre/',views.image_upload,name="imageCaputre"),




]