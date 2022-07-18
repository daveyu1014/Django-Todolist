from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def user_logout(request):
    logout(request)

    return redirect('todo')


def profile(request):
    print(request.user)
    return render(request, './user/profile.html')


def user_login(request):
    message = ''

    if request.method == 'POST':
        if request.POST.get('register'):
            return redirect('register')
    

    if request.POST.get('login'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == '' or password == '':
            message = '帳號密碼不能為空'
        else:
            user = authenticate(username = username, password = password)
            
            if user:
                login(request, user)
                message = '登入成功!'
                return redirect('todo')
            else:
                message = '登入失敗!'


    return render(request, './user/login.html', {'message' : message})


def user_register(request):
    form = UserCreationForm()
    message = ''
    
    if request.method == 'POST':
        username = request.POST.get('username')
        #email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        #print(username, password1, password2)
    
        if password1 !=password2:
            message = '兩次密碼不同'
        elif len(password1) < 8:
            message = '密碼過短(至少八個字)'
        else:
            #使用者名稱是否重複
            
            if User.objects.filter(username = username).exists():
                message = "使用者名稱重複"
            
            #if User.objects.filter(email = email).exists():
            #    message = "此email已註冊"
            
            else:
                user = User.objects.create_user(username = username, password = password1).save()
                
                if user:
                    message = '註冊成功!'
                    login(request, user)
                    return redirect('todo')

    return render(request, './user/register.html', {'form' :form, 'message': message})

    

