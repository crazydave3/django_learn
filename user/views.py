from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
from .userForms import SignUpForm,SignUpModelForm
# Create your views here.


def index(request):
    user_list = User.objects.filter()
    template_name = "index.html"
    context = {
        "user_list": user_list,
    }
    return render(request, template_name, context)

def sign_up(request):
    if request.method == "GET":
        #ModelForm
        # form = SignUpModelForm()
        #Form
        form = SignUpForm()
    return render(request, 'sign_up.html', {"form": form})

def signUp(request):
    #ModelForm
    # form = SignUpModelForm(data=request.POST)
    # form.save()
    #Form
    form = SignUpForm(data=request.POST)
    if form.is_valid():
        data = form.cleaned_data
        user = User(name=data['name'], password=data['password'], email=data['email'])
        user.save()
    else:
        print(form.errors)

    return HttpResponseRedirect("/user/sign_up")