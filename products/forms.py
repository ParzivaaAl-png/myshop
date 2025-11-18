from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'slug', 'description', 'price', 'main_image', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows':4, 'class':'input'}),
            'title': forms.TextInput(attrs={'class':'input'}),
            'slug': forms.TextInput(attrs={'class':'input'}),
            'price': forms.NumberInput(attrs={'class':'input'}),
        }
