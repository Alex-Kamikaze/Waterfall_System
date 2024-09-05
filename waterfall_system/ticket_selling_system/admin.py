from django.contrib import admin
from .models import Ticket, SessionInfo

# Register your models here.
admin.site.register(Ticket)
admin.site.register(SessionInfo)