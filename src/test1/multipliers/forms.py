from django import forms

class OrForm(forms.Form):

    result = forms.IntegerField(label='put_here')

