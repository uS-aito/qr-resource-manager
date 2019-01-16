from django import forms

class RentalForm(forms.Form):
    checkout_date = forms.DateField()
    return_date = forms.DateField()