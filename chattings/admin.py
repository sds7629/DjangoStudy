from django.contrib import admin
from .models import Chatting

@admin.register(Chatting)
class ChattingAdmin(admin.ModelAdmin):
    pass
# Register your models here.
