# orders/forms.py
from django import forms
from .models import Order, CardDesign
from .custom_widgets import ImageRadioSelect




class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'full_name', 'username', 'email', 'phone', 'address',
            'card_design', 'logo', 'name_on_card', 'headline_on_card',
            'phone_on_card'
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'cols': 40}),
            'card_design': ImageRadioSelect,
        }

