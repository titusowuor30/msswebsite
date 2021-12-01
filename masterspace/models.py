from typing import Pattern
from django.db import models

# Create your models here.
#1. services - Overview Tile icon featured
# 2. About - overview description contact-fk  | services-featured services |Team
# 3.partners -Title overview org desc images
# 4.weighbridge - overview howitworks images
### 6. LearnMore - partnerships mss-approach(image) project-management(image) 
###7. Achievements - title
#8. Team - Name Rank Contact social-links(fb,tweeter,in)
#9. FAQ - quiz_title answer
#10. Clients -logos
####12. PRODUCT DEVELOPMENT & MANAGEMENT - steps title  image - description

class Service_modules(models.Model):
    module_title=models.CharField(max_length=100,default='module #2')
    module_subtitle=models.CharField(max_length=255,default='module #2 subtile')
    module_content=models.TextField(max_length=1500,default='module #2 content')
    
    def __str__(self):
            return self.module_title

    class Meta:
        verbose_name_plural='Service Modules' 

class Service_Classification(models.Model):
    title=models.CharField(max_length=255)  
    overview=models.TextField(max_length=500,default="classicficatio description") 
    def __str__(self):
            return self.title

    class Meta:
        verbose_name_plural='Service Classification'      

class Services(models.Model):
    title=models.CharField(max_length=100)
    overview=models.TextField(max_length=255,default='Service short description here...')
    Service_modules=models.ManyToManyField('Service_modules',blank=True,null=True)
    classification=models.ForeignKey('Service_Classification',on_delete=models.CASCADE,related_name='services',blank=True,null=True)
    image=models.ImageField(upload_to='uploads/services/',blank=True,null=True,default='media/default.jpg')
    icon=models.CharField(max_length=255)

    def getImg(self):
        if self.image:
            return self.image.url
        else:
            return 'media/default.jpg' 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural='MSS Services'    

class Location(models.Model):
    building=models.CharField(max_length=100)
    floor=models.CharField(max_length=15,help_text='e.g 3rd,4th,2nd')
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural='Our Location'     

class Social_links(models.Model):
    link_url=models.URLField(max_length=255,default='https://facebook.com')
    icon=models.CharField(max_length=50,help_text='use font awesome icons e.g fas fa-tweeter or fa fa-facebook',blank=True,null=True)
    
    def __str__(self):
        return self.link_url

    class Meta:
        verbose_name_plural='Social Media Links'    

class About(models.Model):
    overview=models.TextField(max_length=500)
    vission=models.TextField(max_length=255)
    mission=models.TextField(max_length=255)
    date_founded=models.DateField(blank=True,null=True)
    location=models.ForeignKey('Location',on_delete=models.CASCADE)
    email=models.EmailField(default='info@masterspace.co.ke')
    phone=models.CharField(max_length=15,help_text='+254{0} xxx xxx xxx',default='+254(0) 773 499 346')
    social_links=models.ManyToManyField('Social_links')
    careers_url=models.URLField(max_length=255,default='https://careers.masterspace.co.ke/')

    def __str__(self):
        return self.overview

    class Meta:
        verbose_name_plural='About MSS & Contacts'  
        
        
class CoreValues(models.Model):
    image=models.ImageField(upload_to="uploads/corevalues/",default='media/default.jpg',blank=True,null=True)
    title=models.CharField(max_length=255,blank=True,default='title')
    content=models.CharField(max_length=255,default='content')
    
    
    def __str__(self):
        return self.title
    
    def getImg(self):
        if self.image:
            return self.image.url
        else:
            return 'media/default.jpg'

    class Meta:
        verbose_name_plural='Core Values'  
    
            

class Partners(models.Model):
    title=models.CharField(max_length=100)
    overview=models.TextField(max_length=255)
    description=models.TextField(max_length=500)
    snipet=models.ImageField(upload_to='uploads/patnership_snipets/',blank=True,null=True)

    def getImg(self):
        if self.snipet:
            return self.logo.url
        else:
            return 'media/default.jpg' 


    def __str__(self):
            return self.title

    class Meta:
        verbose_name_plural='MSS Partnerships'  


    def __str__(self):
            return self.introduction

    class Meta:
        verbose_name_plural='MSS WeighBridge Services'

class Answers(models.Model):
    answer=models.TextField(max_length=255)

    def __str__(self):
        return self.answer
    
    class Meta:
        verbose_name_plural='Answers to FAQs'       


class FAQs(models.Model):
    question=models.TextField(max_length=255)
    answers=models.ManyToManyField('Answers')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural='FAQs & QAs'    

class Clients(models.Model):
    organisation_name=models.CharField(max_length=100)
    website=models.URLField(max_length=500,default='example.com')
    logo=models.ImageField(upload_to='uploads/client_logos/')

    def getImg(self):
        if self.logo:
            return self.logo.url
        else:
            return 'media/default.jpg'    

    def __str__(self):
        return self.logo.url

    class Meta:
        verbose_name_plural='Organisations & Clients' 






    


