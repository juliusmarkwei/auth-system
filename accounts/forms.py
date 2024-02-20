from django import forms


class UserCreateForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    re_password = forms.CharField(
        label="Password confirm", widget=forms.PasswordInput
    )
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
