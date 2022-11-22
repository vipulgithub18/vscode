from django import forms

class Studeform(forms.Form):
    name = forms.CharField(max_length=66)
    age = forms.IntegerField()