from django import forms
from django.shortcuts import redirect, render
from garden.models import PlantDetails

class PlantDetailsForm(forms.Form):
    plant_name = forms.CharField()
    plant_type = forms.CharField()
    plant_price = forms.CharField()
    plant_benefits = forms.CharField()

def index(request):
    return render(request, 'garden/index.html')

def insert(request):
    if request.method == "POST":
        form = PlantDetailsForm(request.POST)
        if form.is_valid():
            plants_details = PlantDetails(**form.cleaned_data)
            plants_details.save()
        return redirect(all)
    form = PlantDetailsForm()
    return render(request, 'garden/insert.html', {'form': form})

def all(request):
    plants = PlantDetails.objects.all()
    return render(request, 'garden/all.html', {'plants': plants})

def edit(request, plant_id):
    if request.method == 'POST':
        form = PlantDetailsForm(request.POST)
        if form.is_valid():
            PlantDetails.objects.filter(id=plant_id).update(**form.cleaned_data)
        return redirect(all)
    plant = PlantDetails.objects.get(id = plant_id)
    form = PlantDetailsForm(plant.__dict__)
    return render(request, 'garden/edit.html', {'form': form})
