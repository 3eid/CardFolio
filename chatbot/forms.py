from django import forms
from .models import Chatbot

class ChatbotForm(forms.ModelForm):
    class Meta:
        model = Chatbot
        fields = ['faq', 'about_me', 'work_examples', 'schedule']
        widgets = {
            'faq': forms.Textarea(attrs={'rows': 5}),
            'about_me': forms.Textarea(attrs={'rows': 5}),
            'work_examples': forms.Textarea(attrs={'rows': 5}),
            'schedule': forms.Textarea(attrs={'rows': 5}),
        }
