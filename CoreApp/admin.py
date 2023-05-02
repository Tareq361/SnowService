from django.contrib import admin

from CoreApp.models import Member, Service, Booking

# Register your models here.
admin.site.register(Member)
admin.site.register(Service)
admin.site.register(Booking)