from django.contrib import admin

# Register your models here.
from .models import Car
from .models import User

admin.site.register(Car)
admin.site.register(User)
