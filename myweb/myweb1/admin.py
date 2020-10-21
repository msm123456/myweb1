from django.contrib import admin
from .models import my_home
from .models import my_about
from .models import resume
from .models import Services
from .models import skills
# Register your models here.
admin.site.register(my_home)
admin.site.register(my_about)
admin.site.register(resume)
admin.site.register(Services)
admin.site.register(skills)