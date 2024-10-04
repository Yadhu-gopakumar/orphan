from django.contrib import admin

# Register your models here.
from .models import feedbform,futuresupport,userdonatedb,feedbackforms

admin.site.register(feedbform) #table registering
admin.site.register(futuresupport) #table registering
admin.site.register(userdonatedb) #table registering
admin.site.register(feedbackforms) #table registering