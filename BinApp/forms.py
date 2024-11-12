# forms.py
from django import forms

class ModifyScriptsForm(forms.Form):
    euro_value = forms.CharField(label='Euro Value', required=True)
    btc_value = forms.CharField(label='BTC Value', required=True)

