from django.contrib import admin

from customuser.models import User, EmployeeProfile, EmployerProfile

# Register your models here.
admin.site.register(User)
admin.site.register(EmployerProfile)
admin.site.register(EmployeeProfile)
