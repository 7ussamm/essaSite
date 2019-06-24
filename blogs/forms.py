from django import forms
from .models import SignUp
# from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = [
            'name',
            'email',
        ]

    def clean_email(self):  # clean is a key argument , i must be clean then add after it the var from the model
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if extension != 'gov':
            raise forms.ValidationError('Please make sure u use Gmail with .gov')
        elif domain != 'gmail':
            raise forms.ValidationError('Please make sure u use Gmail with .gov')
        return email

    def clean_name(self):
        full_name = self.cleaned_data.get('name')
        if len(full_name) > 20:
            raise forms.ValidationError('Please enter your name less than 20 characters ')
        return full_name


class ContactForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 20}))


class Filter(forms.Form):
    name = forms.CharField(max_length=200,
                           label='Filter',
                           widget=forms.TextInput(attrs={'placeholder': 'Enter a name to filter with'}))




