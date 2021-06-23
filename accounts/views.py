from django.shortcuts import redirect, render
from  django.contrib import auth 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    # print(request.user.groups.all())
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user:
            messages.success(request, 'Logged in')
            auth.login(request, user)
        else:
            messages.error(request, 'Incorrect username password combo')
    data = {}
    return render(request, 'accounts/login.html', data)


def logout(request):
    auth.logout(request)
    messages.info(request,'Logged Out')
    return redirect('home')


@login_required(login_url='login')
def register(request):
    
    # if request.user.group.filter(name='Admin'): # Just for making sure that no one creates accounts
    #     return redirect('home')

    data = {}
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.error(request, 'This username already exists in Our Database')
                return redirect('register')

            user = User(
                username=username,
                email=email,
                password=password1
            )

            user.save()
            messages.success(request, 'Account Created Login.')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match')

    return render(request, 'accounts/register.html', data)


@login_required(login_url='login')
def dashboard(request):
    pass