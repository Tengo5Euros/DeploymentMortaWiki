from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MyUser

class MyUserAdmin(UserAdmin):
    model = MyUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')

admin.site.register(MyUser, MyUserAdmin)
