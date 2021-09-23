from django import forms
from .models import UserInfo


class RegisterForm(forms.Form):

    first_name = forms.CharField(max_length=100, label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    username = forms.CharField(max_length=100, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='',
                             widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(
        max_length=100, label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(
        max_length=100, label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmm Password'}))

    def clean_email(self):
        if UserInfo.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("This email already exists")
        return self.cleaned_data['email']

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise forms.ValidationError("Password doesn't match")
        return self.cleaned_data['password2']


class LoginForm(forms.Form):

    username = forms.CharField(label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(
        max_length=100, label='',
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    # def clean_email(self):
    #     if not UserInfo.objects.filter(email= self.cleaned_data['email']).exists():
    #         raise forms.ValidationError("Email Not Found")
    #     return self.cleaned_data['email']


class AddressForm(forms.Form):

    first_name = forms.CharField(max_length=100, label='',
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=100, label='',
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    company = forms.CharField(max_length=100, label='',
                              widget=forms.TextInput(attrs={'placeholder': 'Company'}))
    phone = forms.CharField(max_length=100, label='',
                            widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    address1 = forms.CharField(max_length=100, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Address 1'}))
    address2 = forms.CharField(max_length=100, label='',
                               widget=forms.TextInput(attrs={'placeholder': 'Address 2'}))
    zipcode = forms.CharField(max_length=100, label='',
                              widget=forms.TextInput(attrs={'placeholder': 'Zip Code'}))
    country = forms.CharField(max_length=100, label='',
                              widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    # default = forms.BooleanField(
    #     widget=forms.NullBooleanSelect(attrs={'id': 'default-check'}))
    default = forms.TypedChoiceField(coerce=lambda x: x == 'True',
                                     choices=((False, 'No'), (True, 'Yes')), widget=forms.NullBooleanSelect(attrs={'id': 'default-check'}))
