from django.contrib import admin
from .models import chat, Group
# Register your models here.

@admin.register(chat)
class chatAdmin(admin.ModelAdmin):
    list_display = ('message','message_time','Group_name',)
  
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
      list_display= ('name',)