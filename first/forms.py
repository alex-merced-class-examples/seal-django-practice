from django import forms

## Create a new Form Class for Creating Form
## From a template
class NameAgeForm(forms.Form):
    name = forms.CharField(label="Your Name")
    age = forms.IntegerField(label="Your Age")