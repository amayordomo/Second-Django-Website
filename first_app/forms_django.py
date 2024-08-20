from django import forms 

class user_form(forms.Form):
    user_name = forms.CharField(label="Full Name", widget=forms.TextInput(attrs={'placeholder':"Enter your full name", 'style': "width:300px"}))
    user_dob = forms.DateField(label="Date of Birth", widget=forms.TextInput(attrs={'type' : "date"}))
    user_email = forms.EmailField(label="Email")
    boolean_field = forms.BooleanField(required=False)
    char_field = forms.CharField(max_length=15, min_length=5, widget=forms.TextInput(attrs={'placeholder' : 'min 5 chars, max 15 chars', 'style' : 'width:200px'}))
    
    choices = (('1', 'First'), ('2', 'Second'), ('3', 'Third'))
    choice_field = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
