from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def byeall(request):
    template="index2.html"
    context={}
    return render(request,template,context)

def pavi(request): #using context
    template="index.html"
    a="pavithra"
    context={"o":a,"d":"dinesh5"}
    return render(request,template,context)

def fly(request):
    a=Book.objects.all()
    return render(request,"web.html",{"data":a})



# Create your views he
# Create your views he
# Create your views he
