from django import forms
class RegistrationForm(forms.Form):
    first_name=forms.CharField(
        label="Enter First Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'First Name',
                'class':'form-control'

            }
        )

    )
    last_name=forms.CharField(
        label="Enter Last Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Last Name',
                'class':'form-control'

            }
        )

    )
    username=forms.CharField(
        label="Enter user Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'username',
                'class':'form-control'

            }
        )

    )
    password=forms.CharField(
        label="Enter password",
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'class':'form-control'

            }
        )

    )
    mobile=forms.IntegerField(
        label="Enter Mobile no",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Mobile number',
                'class':'form-control'

            }
        )


    )
    email=forms.EmailField(
        label="Enter Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Email',
                'class':'form-control'

            }
        )

    )
class LoginForm(forms.Form):
    username=forms.CharField(
        label='Enter username',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Username',
                'class':'form-control'
            }
        )
    )
    password=forms.CharField(
        label='Enter password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Password',
                'class':'form-control'
            }
        )
    )


