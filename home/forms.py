from django import forms

class SearchForm(forms.Form):
    search2 = forms.CharField(label='Search', max_length=100)
    catid = forms.IntegerField()
