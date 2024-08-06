from django import forms
from .models import User
from django.core.validators import ValidationError
class EmailValidation:
    def __call__(self, value):
        userList = User.objects.filter(email=value)
        if userList:
            raise ValidationError("this email has been sign up")

class SignUpForm(forms.Form):
    name = forms.CharField(
        label="name",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    password = forms.CharField(
        label="password",
        widget=forms.TextInput(attrs={"class": "form-control"})
    )

    email = forms.CharField(
        label="email",
        widget=forms.EmailInput(attrs={"class": "form-control"}),
        validators=[EmailValidation()]
    )

class SignUpModelForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'password', 'email']
        fields = "__all__"
