from django.contrib import admin
from .models import Departments,Doctor,Booking

admin.site.register(Departments)
admin.site.register(Doctor)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','booking_date','booking_on')
admin.site.register(Booking,BookingAdmin)
