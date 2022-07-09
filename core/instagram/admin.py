from django.contrib import admin
from .models import Logins
from .models import Register
# Register your models here.

admin.site.register(Logins)
admin.site.register(Register)