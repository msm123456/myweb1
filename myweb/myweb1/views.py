from django.shortcuts import render
from django.core.mail import send_mail
from .models import my_home
from .models import my_about
from .models import resume
from .models import Services
def home(request):
    home_ob=my_home.objects.all()
    about_ob=my_about.objects.all()
    my_resume=resume.objects.all()
    my_services=Services.objects.all()
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
        return render(request,'index.html',{"home_ob":home_ob,"about_ob":about_ob,"my_services":my_services,"my_resume":my_resume})
    else:
        return render(request,'index.html',{"home_ob":home_ob,"about_ob":about_ob,"my_services":my_services,"my_resume":my_resume})
        
# Create your views here.


