from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['heading', 'subheading', 'description', 'image', 'is_published']
