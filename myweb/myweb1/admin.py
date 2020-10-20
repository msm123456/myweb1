from django.contrib import admin
from .models import my_home
from .models import my_about
from .models import Services

# Register your models here.
admin.site.register(my_home)
admin.site.register(my_about)
admin.site.register(Services)