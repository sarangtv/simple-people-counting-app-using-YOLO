
from django.db import models

# Create your models here.
choice=(('waiting','waiting'),('approved','approved'),('rejected','rejected'))
class registration(models.Model):

    username=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    # phone=models.CharField(max_length=200,null=True)
    password=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=20,choices=choice)
   