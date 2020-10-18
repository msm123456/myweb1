from django.contrib import admin
from .models import my_home
from .models import my_about

# Register your models here.
admin.site.register(my_home)
admin.site.register(my_about)