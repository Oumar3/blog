from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
# Create your views here.
def loginform(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        user = User.objects.get(email=email)
        if user:
            user = authenticate(request, username=user.username, password=pwd)
            if user is not None:
                login(request, user)
                return redirect('blogapp:home')
    else:
        messages.error(request, "Identifiants incorrects. Veuillez réessayer.")
    return render(request,'login.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)  # Déconnecter l'utilisateur
    return redirect('blogapp:home')

def registerform(request):
    return render(request,'register.html')