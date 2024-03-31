from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView


@login_required
def home(request):
    return render(request, 'home.html', {})

# def signupview(request):
#     if request.method == 'POST':
#          form = UserCreationForm(request.POST)
#          if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request, user)
#             return redirect("home")
#     else:
#         form = UserCreationForm()
#     return render(request, "registration/signup.html", {"form": form})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
def loginView(request):
    return render(request, "registration/login.html")


def signupView(request):
    return render(request, "registration/signup.html")