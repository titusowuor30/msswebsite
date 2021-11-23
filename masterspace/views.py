from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib import messages
from .models import *
import datetime

# Create your views here.
def home(request):
    qas=FAQs.objects.all()
    cms_first=Services.objects.all().first()
    front_office=Services.objects.all()[1:]
    cm_image=cms_first.image.url
    return render(request,'index.html',
    {'cms':front_office,'cms_first':cms_first,
    'cm_image':cm_image,'qas':qas,
    })
    
def search(request):
    query = request.GET.get('query', '')
    service = Services.objects.filter(Q(title__icontains=query) | Q(overview__icontains=query) | Q(classification__icontains=query))

    return render(request, 'search.html', {'service': service, 'query': query})    

def services(request):
    return render(request,'services.html')

def more(request,id):
    service=Services.objects.get(pk=id)
    return render(request, 'more.html',{'service':service})


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')        


def send_message(request):
    if request.method=='POST':
        message=Messages(
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            message=request.POST.get('message')
        )
        message.save()
        messages.success(request,'Messages sent successfully!!\nThank you for contacting Masterspace!')
    return redirect('contact')