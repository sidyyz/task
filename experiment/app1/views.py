from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import mydetails
from django.core.serializers import serialize

def index(request):
          return render(request,'register.html')
def searchpage(request):
          return render(request,'searchpage.html')
def regcod(request):
    name=request.GET.get('name')
    address=request.GET.get('address')
    #m=mydetails(myname=name, mailmyaddr=address)
    #m.save()
    m=mydetails.objects.create(myname=name, myaddress=address)
    if(m!=None):
        data = {'sts':True,'msg':"saved data"}
        return JsonResponse(data)
    else:
        data = {'sts':False,'msg':"error..failed"}
        return JsonResponse(data)
    
def fillname(request):
    data1=mydetails.objects.all()
    data = serialize("json", data1)
    return JsonResponse(data,safe=False)

def searchcontent(request):
    nme=request.GET.get('nme')
    dataout=mydetails.objects.filter(myname=nme)
    data = serialize("json", dataout)
    return JsonResponse(data,safe=False)

def updatecontent(request):
    nme=request.GET.get('nme')
    addr=request.GET.get('addr')
    dbobj=mydetails.objects.filter(myname=nme)
    dbobj.update(myaddress=addr)
    if(dbobj!=None):
        data = {'sts':True,'msg':"saved data"}
        return JsonResponse(data)
    else:
        data = {'sts':False,'msg':"error..failed"}
        return JsonResponse(data)
    

   