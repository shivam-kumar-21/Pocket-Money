from django.contrib import admin
from students import models 
# Register your models here.

from django.contrib import admin
from .models import Student, Student_Detail
from django.utils.html import format_html

class StudentDetailAdmin(admin.ModelAdmin):
    list_display = ('student', 'last_paid_date', 'last_paid_amount', 'total_paid_amount', 'remaining_balance', 'view_transaction_history')

    readonly_fields = ('student', 'last_paid_date', 'last_paid_amount', 'total_paid_amount', 'remaining_balance', 'transaction_history', 'additional_info')

    def view_transaction_history(self, obj):
        return format_html('<pre>{}</pre>', obj.transaction_history)

    view_transaction_history.short_description = 'Transaction History'

admin.site.register(models.Student)
admin.site.register(models.Student_Detail, StudentDetailAdmin)

