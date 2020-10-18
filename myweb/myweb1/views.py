from django.shortcuts import render
from django.core.mail import send_mail
from .models import my_home
from .models import my_about
def home(request):
    home_ob=my_home.objects.all()
    about_ob=my_about.objects.all()
    if request.POST:
        subject=request.POST["subject"]+" from "+request.POST['name']
        message=request.POST["message"]
        email=request.POST["email"]
        send_mail(
            subject,
            message,
            email,
            ['dr737944@gmail.com'],
        #fail_silently=True
        )
        return render(request,'index.html',{"home_ob":home_ob,"about_ob":about_ob})
    else:
        return render(request,'index.html',{"home_ob":home_ob,"about_ob":about_ob})
        
# Create your views here.


