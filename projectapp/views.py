from os import name
from django.shortcuts import redirect,render
from .models import *
from .forms import *
from django.core.files.storage import FileSystemStorage
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("sarangtv2001@gmail.com", "ttodzanzrxggqqpp")

# message to be sent
message = "Over crowd detected"

# sending the mail


from urllib.request import urlopen
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import numpy as np
import csv
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from PIL import Image
import keras
import tensorflow as tf
from tensorflow.keras import backend
from tensorflow.keras.models import Model,Sequential,load_model
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Dense,Flatten,Dropout,BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.optimizers import SGD
q=""
from tensorflow import keras

def index(request):
    return render(request,'index.html')
    

def about(request):
    return render(request,'about.html')


def login(request):
    return render(request,'login.html')


def home(request):
    return render(request,'home.html')



def contact(request):
    return render(request,'contact.html')


def fruit(request):
    return render(request,'fruit.html')




def register(request):
    if request.method=="POST":    
       
        username=request.POST.get('name')
        email=request.POST.get('email')
        # phonenuumber=request.POST.get('phone')
        password=request.POST.get('password')
        status="waiting"
        
        registration(username=username,email=email,password=password,status=status).save()
        return redirect('login')
    else:
      return render(request,'index')

def log(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        status="approved"
        cr=registration.objects.filter(username=username,password=password,status=status)
        if cr:
            user=registration.objects.get(username=username,password=password)
            id=user.id
            username=user.username
            password=user.password
            request.session['id']=id
            request.session['username']=username
            request.session['password']=password
            # request.session['address']=address
            # request.session['gender']=gender
           
            return redirect('imageCaputre')
        else:
            return render(request,'login.html')
    else:
        return render(request,'register.html')

def file(request):
    result=""
    x=""
    y=""
    q=""
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded = fs.url(filename)
        print('uploaded',myfile.name)
        request.session['file']=myfile.name
        fn=myfile.name
        q="E:\\pmidhunfisat\\Frontend\\media\\" + fn


        image = cv2.imread(q)
        #image = cv2.imread(q)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# read haacascade to detect faces in input image
        face_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_alt.xml')

# detects faces in the input image
        faces = face_cascade.detectMultiScale(gray, 1.1, 2)
        print('Number of detected persons:', len(faces))\

# loop over all the detected faces
        for (x,y,w,h) in faces:
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)
        count=len(faces)
        if count>5:
            s.sendmail("sarangtv2001@gmail.com", "sarangstreakzz@gmail.com", message)

# terminating the session
            s.quit()

        
        return render(request, 'fileresult.html', {'uploaded':fn,'level':len(faces)})

       
    return render(request,'file.html')


def fileresult(request):
    return render(request,'fileresult.html')

def image_upload(request):
    q=""
    faces=""
    context = dict()
    if request.method == 'POST':
        username = "data"
        image_path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
        image = NamedTemporaryFile()
        image.write(urlopen(image_path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'  # store image in jpeg format
        image.name = name
        q="C:\\Users\\HP\\Desktop\\Frontend\\media\\" + name
        grade=''
        if image is not None:
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded = fs.url(filename)
            print('uploaded',image.name)
            #obj = Image.objects.create(username=username, image=image)  # create a object of Image type defined in your model
            #obj.save()
            context["path"] = image_path  #url to image stored in my server/local device
            context["username"] = username


            image = cv2.imread(q)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# read haacascade to detect faces in input image
            face_cascade = cv2.CascadeClassifier('C:\\Users\\HP\\Desktop\\Frontend\\models\\haarcascade_frontalface_alt.xml')

# detects faces in the input image
            faces = face_cascade.detectMultiScale(gray, 1.1, 2)
            print('Number of detected persons:', len(faces))\

# loop over all the detected faces
            for (x,y,w,h) in faces:
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,255),2)

   # To draw a rectangle around the detected face  



                #return render(request, 'fileresult.html', {'uploaded':class_name,'level':level,'category':category,'grade':grade})
           
            return render(request, 'fileresult.html', {'uploaded':q,'level':len(faces)})

        
    return render(request, 'imageCaputre.html', context=context)  # context is like respose data we are sending back to user, that wi