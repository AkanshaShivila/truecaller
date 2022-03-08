from django.shortcuts import render,HttpResponse
from .models import Person
import phonenumbers
from phonenumbers import geocoder,carrier

def home(request):
    technical={}
    if request.method=='POST':
        ph_num = request.POST.get('number','')
        a = Person(phone_no=ph_num)
        a.save()

        phone_num = phonenumbers.parse(ph_num,None)
        country=geocoder.description_for_number(phone_num, 'en')
        sim_provider = carrier.name_for_number(phone_num, 'en')
        technical['country']=country
        technical['sim_provider']= sim_provider
        technical['phone'] = phone_num

    return render(request,'index.html',technical)
