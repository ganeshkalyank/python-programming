from django.forms import CharField, Form
from django.shortcuts import redirect, render
from .models import Member

# Create your views here.

def index(request):
    return render(request, "members/index.html")

def all(request):
    members = Member.objects.all()
    return render(request, "members/all.html", {"members": members})

def add(request):
    if request.method == "GET":
        return render(request, "members/add.html")
    else:
        data = request.POST
        newm = Member(
            AadharNumber = data['AadharNumber'],
            Name = data['Name'],
            Age = data['Age'],
            Address = data['Address'],
            NativePlace = data['NativePlace'],
            MobileNumber = data['MobileNumber']
        )
        newm.save()
        return redirect(all)
    
def get(request):
    if 'MobileNumber' in request.GET.keys():
        m = Member.objects.filter(MobileNumber = request.GET['MobileNumber']).first()
        return render(request, "members/get.html", {"m": m})
    else:
        return render(request, "members/get.html")