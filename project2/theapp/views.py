from django.shortcuts import render,redirect
from django.http import HttpResponse
from  . models import details
from . forms import theform

# Create your views here.
def home(request):
    marks=details.objects.all()
    return render(request,"main.html",{'marks':marks})


def form(request):
    if request.method == "POST":
        name=request.POST.get('Name')
        mark1=request.POST.get('Mark1')
        mark2=request.POST.get('mark2')

        marks=details(Name=name,Mark1=mark1,mark2=mark2,)
        marks.save()
        return redirect('/')
    
    return render(request,'form.html',)

def update(request,id):
    max=details.objects.get(id=id)
    form= theform(request.POST or None,instance=max)
    if form.is_valid():
          form.save()
          return redirect('/')
      
    return render(request,'update.html',{'form':form,'max':max})

def delete(request,id):
    if request.method=="POST":
        dele=details.objects.get(id=id)
        dele.delete()
        return redirect('/')
    return render (request,'delete.html')

def detail(request,id):
    dat=details.objects.get(id=id)
    return render(request,"detail.html",{'dat':dat})
