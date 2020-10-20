from django.db import models

# Create your models here.
class  my_home(models.Model):
    myname=models.CharField(max_length=100)
    bio=models.CharField(max_length=100)
    bio1=models.CharField(max_length=100)
    homepic=models.ImageField(upload_to="image/",default='')
    homepic1=models.ImageField(upload_to="image/",default='')
class  my_about(models.Model):
    aboutpic=models.ImageField(upload_to="image/",default='')
    name=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phonenumber=models.CharField(max_length=100)
    completed_projects=models.CharField(max_length=15)
class  Services(models.Model):
    Servicetext=models.CharField(max_length=100)
    Service1=models.CharField(max_length=100)
    Service2=models.CharField(max_length=100)
    Service3=models.CharField(max_length=100)
    Service4=models.CharField(max_length=100)
    Service5=models.CharField(max_length=100)
    Service6=models.CharField(max_length=100)
# class  About(models.Model):
#     image=models.ImageField(upload_to="image/",default='')
#     image1=models.ImageField(upload_to="image/",default='')
# class  Resume(models.Model):
#     image=models.ImageField(upload_to="image/",default='')
#     image1=models.ImageField(upload_to="image/",default='')
# class  Skills(models.Model):
#     image=models.ImageField(upload_to="image/",default='')
#     image1=models.ImageField(upload_to="image/",default='')
# class  Projects(models.Model):
#     image=models.ImageField(upload_to="image/",default='')
#     image1=models.ImageField(upload_to="image/",default='')
# class  My_Blog(models.Model):
#     image=models.ImageField(upload_to="image/",default='')
#     image1=models.ImageField(upload_to="image/",default='')
# class  Contact(models.Model):
#     image=models.ImageField(upload_to="image/",default='')
#     image1=models.ImageField(upload_to="image/",default='')