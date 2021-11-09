from .models import  *
from django.db.models import Q

def contact(request):
    about=About.objects.all().first()
    about_fb=Social_links.objects.get(Q(link_url__icontains='facebook'))
    about_tweeter=Social_links.objects.get(Q(link_url__icontains='tweeter'))
    about_in=Social_links.objects.get(Q(link_url__icontains='linkedin'))
    about_insta=Social_links.objects.get(Q(link_url__icontains='instagram') | Q(link_url__icontains='insta'))
    context={
        'fb':about_fb,
        'twit':about_tweeter,
        'linkedin':about_in,
        'insta':about_insta,
        'abt':about
    }
    print(about_fb)
    return context

def team(request):
    management=Team.objects.all().filter(bod_status=True)
    teams=Team.objects.all()
    return {'tm':management,'teams':teams}    

def clients(request):
    cls=Clients.objects.all()
    return {'cls':cls}      

def services(request):
    allservices=Services.objects.all()
    f_services=Services.objects.all().filter(classification='Featured')[:3]
    c_services=Services.objects.all().filter(classification='Core')[:3]
    n_services=Services.objects.all().filter(classification='New')[:3]
     
    context={
        'allservices':allservices,
        'f_services':f_services,
        'c_services':c_services,
        'n_services':n_services
    } 

    return context