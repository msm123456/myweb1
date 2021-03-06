from django.shortcuts import render
from django.core.mail import send_mail
from .models import my_home
from .models import my_about
from .models import resume
from .models import Services
from .models import skills
from .models import projects
from .models import blog
from .models import contact
def home(request):
    home_ob=my_home.objects.all()
    about_ob=my_about.objects.all()
    my_resume=resume.objects.all()
    my_services=Services.objects.all()
    my_skills=skills.objects.all()
    my_projects=projects.objects.all()
    my_blog=blog.objects.all()
    my_contact=contact.objects.all()
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
        return render(request,'index.html',{"home_ob":home_ob,"about_ob":about_ob,"my_services":my_services,"my_resume":my_resume,"my_skills":my_skills,"my_projects":my_projects,"my_blog":my_blog,"my_contact":my_contact})
    else:
        return render(request,'index.html',{"home_ob":home_ob,"about_ob":about_ob,"my_services":my_services,"my_resume":my_resume,"my_skills":my_skills,"my_projects":my_projects,"my_blog":my_blog,"my_contact":my_contact})
        
# Create your views here.
