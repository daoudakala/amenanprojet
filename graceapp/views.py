from django.shortcuts import render
from django.http import HttpResponse
from .forms import ClientForm

# Create your views here.

def home(request):
    return render(request,'index.html')


def base(request):
    return render(request,'base.html')


def index(request):
    
    form = ClientForm()

    if request.method =='POST':
        form=ClientForm(request.POST)
        if form.is_valid():
            form.save()
    context ={'form':form}  
    return render (request,'index.html',context)      