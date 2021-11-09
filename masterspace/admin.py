from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import *

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display=['overview','vission','mission']
    search_fields=['overview','vission','mission']
admin.site.register(About,AboutAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display=['building','floor','street','city']
    search_fields=['building','floor','street','city']
admin.site.register(Location,LocationAdmin)

class SocialAdmin(admin.ModelAdmin):
    list_display=['link_url']
    search_fields=['link_url']
admin.site.register(Social_links,SocialAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display=['title','classification']
    search_fields=['title','classification']
admin.site.register(Services,ServiceAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display=['name','rank','contact','image']
    search_fields=['name','rank','contact']
admin.site.register(Team,TeamAdmin)


class ClientsAdmin(admin.ModelAdmin):
    list_display=['organisation_name','logo']
    search_fields=['organisation_name']
admin.site.register(Clients,ClientsAdmin)

class FAQsAdmin(admin.ModelAdmin):
    list_display=['question']
    search_fields=['question']
admin.site.register(FAQs,FAQsAdmin)

class AnswersAdmin(admin.ModelAdmin):
    list_display=['answer']
    search_fields=['answer']
admin.site.register(Answers,AnswersAdmin)


class SvModulesAdmin(admin.ModelAdmin):
    list_display=['module_title','module_subtitle','module_content']
admin.site.register(Service_modules,SvModulesAdmin)

class MessagesAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','message']
admin.site.register(Messages,MessagesAdmin)
