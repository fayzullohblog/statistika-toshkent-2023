from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from .form.forms import AccountForm,LoginForm
from .manager import AccountManager
from django.contrib import messages


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
                return redirect('index')
            else:
                messages.error(request,'Invalid username or password')
        
    context={'form':form}
    return render(request=request,template_name='register/login.html',context=context)