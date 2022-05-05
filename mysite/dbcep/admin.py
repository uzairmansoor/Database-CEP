from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Manager)
admin.site.register(Employees)
admin.site.register(Hotel_Branches)
admin.site.register(Rooms)
admin.site.register(Customers)
admin.site.register(Dependents)
admin.site.register(Booking)

