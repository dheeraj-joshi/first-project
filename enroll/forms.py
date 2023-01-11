from django import forms
class Studentregistration(forms.Form):
    name=forms.CharField(max_length=255,min_length=5)
    password=forms.CharField(max_length=9,min_length=8)
    clss=forms.CharField(max_length=20,min_length=2)
    roll=forms.IntegerField(min_value=2,max_value=3)
    email=forms.EmailField()
    agree=forms.BooleanField(label_suffix="",label="i agree")
    price=forms.DecimalField(min_value=5,max_value=40)
    
