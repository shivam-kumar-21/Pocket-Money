from django.contrib import admin
from .models import Student, CustomUser
from django.contrib.auth.admin import UserAdmin


class StudentProfileInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = 'Student Profile'

class CustomUserAdmin(UserAdmin):
    inlines = (StudentProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'role')
    list_filter = ('role',)
    
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Student)
