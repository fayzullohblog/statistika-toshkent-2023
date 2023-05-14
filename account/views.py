from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render,redirect
from .form.forms import AccountForm,LoginForm
from .manager import AccountManager
from django.contrib import messages
from common.choose import UserChoices


# Create your views here.login() takes 1 positional argument but 2 were given


def register(request):
    form=AccountForm()
    if request.method !='POST':
        form=AccountForm()
    else:
        form=AccountForm(request.POST)
        print('is_valid',form.is_valid())
        if form.is_valid():
            form.save()
            message='Hi {form.username}, You have Signed in'
            return redirect('login')
        else:
            message='You Failed'
    context={'form':form}
    return render(request=request,template_name='register/register.html',context=context)

def login_view(request):
    form=LoginForm()
    if request.method != "POST":
        form=LoginForm()
    else:
        form=LoginForm(request.POST)
   
        if form.is_valid():

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            print(username,password,user)
            if user is not None:
                login(request,user)
                if request.user.user == UserChoices.OWNER:
                    return redirect('index')
                return redirect('staff_zip')
                
            else:
                messages.error(request,'Invalid username or password')
        
    context={'form':form}
    return render(request=request,template_name='register/login.html',context=context)

def logout_view(request):
    logout(request)
    return redirect('login')
