# news/forms.py
from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['headline', 'content', 'publication_date', 'image']
