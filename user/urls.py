from django.urls import path
from . import views

# app_name = "user"
urlpatterns = [
    path("",views.index, name="index"),
    path("sign_up",views.sign_up,name="sign_up"),
    path("signUp",views.signUp,name="signUp"),
]