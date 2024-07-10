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
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'card_design': ImageRadioSelect,
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'name_on_card': forms.TextInput(attrs={'class': 'form-control'}),
            'headline_on_card': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_on_card': forms.TextInput(attrs={'class': 'form-control'}),
        }
