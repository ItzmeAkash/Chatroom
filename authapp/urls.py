from django.urls import path,include
from .views import SignUpView,home
from django.views.generic.base import TemplateView 


urlpatterns = [
    path("",home, name="home"),
    path("accounts/signup/", SignUpView.as_view(), name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    
]