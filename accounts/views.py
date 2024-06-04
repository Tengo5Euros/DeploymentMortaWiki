from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MyUserCreationForm, LoginForm

def user_signup(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mortalweb:index')  
    else:
        form = MyUserCreationForm()
    return render(request, 'signup.html', {'form': form})




def user_login(request):
    if request.user.is_authenticated:
        return redirect(reverse("mortalweb:index"))
    message = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect(reverse("mortalweb:index"))
            else:
                message = "Nombre y/o contraseña no válidos"
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("mortalweb:index"))

