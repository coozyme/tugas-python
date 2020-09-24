from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


# class home(TemplateView):
#     templates = 'home.html'

def home(request):
    # return render(request,"home.html", {})
    # return render_to_response("templates/home.html",{"new_app_form":NewAppFormSet()})
    return render(request,'home.html')
def nim1(request):
    return render(request,'nim1.html')

def nim2(request):
    return render(request,'nim2.html')

def nim3(request):
    return render(request,'nim3.html')