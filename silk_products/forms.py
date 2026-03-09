from django import forms

class SilkProductForm(forms.Form):
    PRODUCT_TYPES = [
        ('saree', 'Saree'),
        ('fabric', 'Fabric'),
        ('scarf', 'Scarf'),
    ]
    name = forms.CharField(max_length=200)
    type = forms.ChoiceField(choices=PRODUCT_TYPES)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    availability = forms.BooleanField(required=False, initial=True)
