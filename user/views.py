from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django import forms
from .models import User
# Create your views here.
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
        widget=forms.EmailInput(attrs={"class": "form-control"})
    )

class SignUpModelForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = ['name', 'password', 'email']
        fields = "__all__"


def index(request):
    user_list = User.objects.filter()
    print(user_list,'user_list')
    template_name = "index.html"
    context = {
        "user_list": user_list,
    }
    return render(request, template_name, context)

def sign_up(request):
    if request.method == "GET":
        #ModelForm
        form = SignUpModelForm()
        #Form
        # form = SignUpForm()
    return render(request, 'sign_up.html', {"form": form})

def signUp(request):
    #ModelForm
    form = SignUpModelForm(data=request.POST)
    form.save()
    #Form
    # form = SignUpForm(data=request.POST)
    # if form.is_valid():
    #     data = form.cleaned_data
    #     user = User(name=data['name'], password=data['password'], email=data['email'])
    #     user.save()
    # else:
    #     print(form.errors)

    return HttpResponseRedirect("/user")