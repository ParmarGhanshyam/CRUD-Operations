from django import forms

# creating a form
class GeeksForm(forms.Form):
    StudentId = forms.CharField()
    StudnetName = forms.CharField()
    StudnetNickName =forms.CharField()

