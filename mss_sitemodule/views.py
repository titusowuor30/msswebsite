from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html')

def services(request):
    return render(request,'services.html')


def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')        

def more(request):
    return render(request,'more.html')            