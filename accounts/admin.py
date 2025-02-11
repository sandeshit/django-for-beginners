from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','age','is_staff',]
    fieldsets = UserAdmin.fieldsets + ((None, {'fields':('age',)}),)
    add_fieldsets = ((None,{'classes': ('wide',),'fields': ('username','email','age', 'password1', 'password2'),},),)



admin.site.register(CustomUser, CustomUserAdmin)