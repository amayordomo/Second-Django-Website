from django import forms 
from django.core import validators

class user_form(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(10), validators.MinLengthValidator(5)])
    number_field = forms.IntegerField(validators=[validators.MaxValueValidator(10), validators.MinValueValidator(0)])
    user_email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Your email'}))
    user_vmail = forms.EmailField(label='Confirm Email', widget=forms.TextInput(attrs={'placeholder': 'Confirm email'}))

    def clean(self):
        all_cleaned_data = super().clean()
        user_email = all_cleaned_data['user_email']
        user_vmail = all_cleaned_data['user_vmail']

        if user_email != user_vmail:
            raise forms.ValidationError("Please confirm your email! Fields don't match")

        