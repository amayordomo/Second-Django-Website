from django import forms 

class user_form(forms.Form):
    user_name = forms.CharField(label="Full Name", widget=forms.TextInput(attrs={'placeholder':"Enter your full name", 'style': "width:300px"}))
    user_dob = forms.DateField(label="Date of Birth", widget=forms.TextInput(attrs={'type' : "date"}))
    user_email = forms.EmailField(label="Email")

