from django import forms

TYPE_CHOICES = (
    ("Car","Car"),
    ("Bike","Bike")
)

PAYMENT_CHOICES = (
    ("Card","Card"),
    ("Net Banking", "Net Banking"),
    ("Cash On Delivery", "Cash On Delivery"),
)

class SellForm(forms.Form):
    name = forms.CharField()
    contact_number = forms.IntegerField()
    vehicle_type = forms.ChoiceField(choices=TYPE_CHOICES)
    brand = forms.CharField()
    model_name = forms.CharField()
    year_of_purchase = forms.IntegerField()
    kilometers = forms.IntegerField()
    color = forms.CharField()
    registered_state = forms.CharField()
    no_of_owners = forms.IntegerField()
    base_price = forms.IntegerField()
    mode_of_payment = forms.ChoiceField(choices=PAYMENT_CHOICES)

class BuyForm(forms.Form):
    vehicle_type = forms.ChoiceField(choices=TYPE_CHOICES)
    brand = forms.CharField()
    km_from = forms.IntegerField()
    km_to = forms.IntegerField()
    no_of_owners = forms.IntegerField()
    price_from = forms.IntegerField()
    price_to = forms.IntegerField()
