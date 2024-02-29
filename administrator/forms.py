from django import forms

class loginForm(forms.Form):
    username = forms.CharField(
        max_length = 15,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'username',
                'placeholder': 'Enter "admin" for default',
            }
        )
    )
    password = forms.CharField(
        max_length = 15,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'password',
                'type': 'password',
                'placeholder': 'Enter "1234" for default',
            }
        )
    )

class CenterEdit(forms.Form):
    centerCode = forms.CharField(
        max_length = 25,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'centercode',
                'placeholder': 'Center Code',
            }
        )
    )
    centerName = forms.CharField(
        max_length = 15,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'centername',
                'placeholder': 'Center Name',
            }
        )
    )
    centerLocation = forms.CharField(
        max_length = 15,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'centerlocation',
                'placeholder': 'Center Address',
            }
        )
    )
    vaccineName = forms.CharField(
        max_length = 15,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'vaccinename',
                'placeholder': 'Vaccine Name',
            }
        )
    )
    availableDoseCount = forms.CharField(
        max_length = 15,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'dosecount',
                'placeholder': 'Number of Doses',
            }
        )
    )
    openingTime = forms.CharField(
        max_length = 15,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'openingtime',
                'placeholder': 'Opening Time',
            }
        )
    )
    closingTime = forms.CharField(
        max_length = 15,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'closingtime',
                'placeholder': 'Closing Time',
            }
        )
    )

class DeleteCenter(forms.Form):
    code = forms.CharField()