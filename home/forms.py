from django import forms
from .models import SpecialOfferEmail

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control'}))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone', 'class': 'form-control'}))
    service = forms.ChoiceField(
        choices=[
            ('', 'Type of Service'),
            ('Central System Installation', 'Central System Installation'),
            ('Window Unit Installation', 'Window Unit Installation'),
            ('Wall Unit Installation', 'Wall Unit Installation'),
            ('Maintenance, Support and Repair', 'Maintenance, Support and Repair'),
            ('Other', 'Other'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your Message', 'class': 'form-control'}))

class SpecialOfferEmailForm(forms.ModelForm):
    class Meta:
        model = SpecialOfferEmail
        fields = ['email']

