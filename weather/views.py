from django.shortcuts import render,get_object_or_404,render_to_response
from django.http import HttpResponse
from . models import Location
import requests,json


def index(request):
    return render(request,'weather/index.html')

def find(request):
    code=None
    if request.method=="GET":

        code=request.GET.get('Location')
        country=request.GET.get('Country')

    data = {'zip': str(code) + ','+ str(country),'appid': 'e913baa7097c2f6aff9fc7522b2bb095'}
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?', params=data)
    data = json.loads(r.text)
    tempk = (data['main']['temp'])
    tempInCel = float(tempk - 273.15)
    x={"pin":code,"tempInCel":tempInCel}
    context={"code":code,"tempInCel":str(tempInCel),"Country":country}
    return render_to_response("weather/weath.html",context)




