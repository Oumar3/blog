from django.shortcuts import render,get_object_or_404,redirect
from .models import CustomUser
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.views import View
from .forms import RegisterForm
# Create your views here.
def loginform(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        pwd = request.POST.get('pwd')
        user = authenticate(request, email=email, password=pwd)
        if user is not None:
            login(request, user)
            messages.success(request, "You are connected.")
            return redirect('blogapp:home')
    return render(request,'login.html')

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)  # Déconnecter l'utilisateur
        messages.success(request, "You are disconnected.")

    return redirect('blogapp:home')

# class RegisterView(View):

#     def get(self, request, *args, **kwargs):
#         form = RegisterForm()
#         return render(request, 'register.html', {'form': form})
    

#     def post(self, request, *args, **kwargs):
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('auth:loginin')
#         return self.get(request, *args, **kwargs)
    

def registerform(request, *args, **kwargs):
    if request.method == 'POST':
        #firstname,lastname,email,password,password2
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request,'email exist deja')
            return render(request, 'register1.html') 
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request,'User exist deja')
            return render(request, 'register1.html')
        
        if password != password2:
            messages.error(request,'Le deux mot de passe sont different')
            return render(request, 'register1.html')
        try:
            user = CustomUser.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email,password=password)
        except:
            messages.success(request, "User not created...")
            return render(request, 'register1.html')
        if user is not None:
            messages.success(request, "Inscription réussie !")
            return redirect('auth:loginin')
    return render(request,'register1.html')