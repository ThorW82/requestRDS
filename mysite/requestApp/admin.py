from django.contrib import admin

from requestApp.models import *


#
class RequestAdmin(admin.ModelAdmin):
    mylist = ('id','req_date', 'pay_date','user', 'target', 'sum', 'is_ready')
    list_display = mylist + ('is_agreed',)
    list_display_links = mylist


class AgreedAdmin(admin.ModelAdmin):
    mylist = ('req','user',  'date')
    list_display = mylist
    list_display_links = mylist


class MessageAdmin(admin.ModelAdmin):
    mylist = ('req', 'date','message_text')
    list_display = mylist
    list_display_links = mylist


admin.site.register(Req, RequestAdmin)
admin.site.register(Agreed, AgreedAdmin)
admin.site.register(Message, MessageAdmin)
