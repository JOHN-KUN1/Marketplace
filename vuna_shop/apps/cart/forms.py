from django import forms

class CheckoutForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=255)
    hostel = forms.CharField(max_length=255)
    room = forms.CharField(max_length=255)
    stripe_token = forms.CharField(max_length=255)