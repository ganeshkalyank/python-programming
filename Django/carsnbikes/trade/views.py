from django.shortcuts import redirect, render
from trade.forms import BuyForm, SellForm
from trade.models import Vehicle

def index(request):
    return render(request, "trade/index.html")

def sell(request):
    if request.method == "POST":
        f = SellForm(request.POST)
        if f.is_valid():
            sf = Vehicle(**f.cleaned_data)
            sf.save()
        return redirect(index)
    return render(request, "trade/sell.html", {"form": SellForm})

def buy(request):
    if request.method == "POST":
        f = BuyForm(request.POST)
        if f.is_valid():
            vehicles = Vehicle.objects.filter(
                vehicle_type = f.cleaned_data['vehicle_type'],
                brand = f.cleaned_data['brand'],
                kilometers__gte = f.cleaned_data['km_from'],
                kilometers__lte = f.cleaned_data['km_to'],
                no_of_owners = f.cleaned_data['no_of_owners'],
                base_price__gte = f.cleaned_data['price_from'],
                base_price__lte = f.cleaned_data['price_to'],
            )
            print(vehicles.values())
            return render(request, "trade/list.html", {"vehicles": vehicles})
    return render(request, "trade/buy.html", {"form": BuyForm})
