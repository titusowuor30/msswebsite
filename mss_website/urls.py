"""mss_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from django.conf import settings
from django.contrib.staticfiles.urls import static
from masterspace.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('search/',search, name='search'),
    path('support_services/',support_services,name='support_services'),
    path('request_service/',request_service,name='request_service'),
    path('contact/',contact,name='contact'),
    path('about/',about,name='about'),
    path('more/service/<int:id>/',more,name='more'),
    path('send/message/',send_message,name='message'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header  =  "Masterspace Administration"  
admin.site.site_title  =  "MSS admin site"
admin.site.index_title  =  "MSS Admin"