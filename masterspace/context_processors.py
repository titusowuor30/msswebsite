from .models import  *
from django.db.models import Q

def contact(request):
    about=About.objects.all().first()
    corevalues=CoreValues.objects.all()
    social_links=Social_links.objects.all()
    context={
        'abt':about,
        'corevalues':corevalues,
        'social_links':social_links,
    }
    return context

def clients(request):
    cls=Clients.objects.all()
    return {'cls':cls}      

def services(request):
    allservices=Services.objects.all()
    service_classes=Service_Classification.objects.all()
     
    context={
        'allservices':allservices,
        'service_classes':service_classes,
    } 

    return context