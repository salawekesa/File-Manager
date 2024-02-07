from django import forms

class search_file(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
