from django.shortcuts import render,redirect
from django.http import HttpResponse
from  . models import data
from . forms import theform

# Create your views here.
def home(request):
    marks=data.objects.all()
    return render(request,"main.html",{'marks':marks})


def form(request):
    if request.method == "POST":
        name=request.POST.get('Name')
        regno=request.POST.get('RegNo')
        mark1=request.POST.get('Mark1')
        mark2=request.POST.get('Mark2')
        mark3=request.POST.get('Mark3')

        marks=data(Name=name,RegNo=regno,Mark1=mark1,Mark2=mark2,Mark3=mark3)
        marks.save()
        return redirect('/')
    
    return render(request,'form.html',)

def update(request,id):
    max=data.objects.get(id=id)
    form= theform(request.POST or None,instance=max)
    if form.is_valid():
          form.save()
          return redirect('/')
      
    return render(request,'update.html',{'form':form,'max':max})

def delete(request,id):
    if request.method=="POST":
        dele=data.objects.get(id=id)
        dele.delete()
        return redirect('/')
    return render (request,'delete.html')

def detail(request,id):
    dat=data.objects.get(id=id)
    return render(request,"detail.html",{'dat':dat})
