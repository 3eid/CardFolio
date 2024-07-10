from django import forms
from .models import Chatbot

class ChatbotForm(forms.ModelForm):
    class Meta:
        model = Chatbot
        fields = ['faq', 'about_me', 'work_examples', 'schedule']
        
        widgets = {
            'faq': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            
            'about_me': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            
            'work_examples': forms.Textarea(attrs={'class': 'form-control', 'rows':4 }),
            'schedule': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
