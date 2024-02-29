from django import forms

class UserLogin(forms.Form):
    username = forms.CharField(
        max_length = 20,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'username',
                'placeholder': 'Username',
            }
        )
    )
    password = forms.CharField(
        max_length = 20,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'password',
                'placeholder': 'Password',
                'type': 'password',
            }
        )
    )

class UserRegister(forms.Form):
    name = forms.CharField(
        max_length = 30,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'name',
                'placeholder': 'Name'
            }
        )
    )
    username = forms.CharField(
        max_length = 30,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'username',
                'placeholder': 'Username'
            }
        )
    )
    email = forms.EmailField(
        max_length = 30,
        label = '',
        widget = forms.EmailInput(
            attrs = {
                'id': 'email',
                'placeholder': 'Email'
            }
        )
    )
    password = forms.CharField(
        max_length = 20,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'password',
                'placeholder': 'Password',
                'type': 'password',
            }
        )
    )
    address = forms.CharField(
        max_length = 50,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'address',
                'placeholder': 'Address'
            }
        )
    )

class SlotBooking(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    vaccine = forms.CharField()
    date = forms.CharField()
    code = forms.CharField()