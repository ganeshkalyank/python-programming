from django.shortcuts import render

from .models import Details

# Create your views here.

def addentry(request):
    if request.method == "GET":
        details = Details.objects.order_by("id")
        context = {"details":details}
        return render(request, "details/index.html",context)
    else:
        name = request.POST['name']
        mobile = request.POST['mobile']
        details = Details(name=name, mobile=mobile)
        details.save()
        details = Details.objects.order_by("name")
        context = {"details":details}
        return render(request, "details/index.html",context)
