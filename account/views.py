from django.contrib.auth import login,authenticate
from django.shortcuts import render,redirect
from .form.forms import AccountForm,LoginForm
from .manager import AccountManager


# Create your views here.
def login(request):
    return render(request=request,template_name='register/login.html')


def register(request):
    # if request.user.is_authenticated:

    form=AccountForm()
    if request.method !='POST':
        form=AccountForm()
    else:
        form=AccountForm(request.POST)
        if form.is_valid():
            form.save()
            message='Hi {form.username}, You have Signed in'
            return redirect('login')
        else:
            message='You Failed'

            
    context={'form':form}
             
    return render(request=request,template_name='register/register.html',context=context)

def login(request):
    form=LoginForm()
    if request.method != "POST":
        form=LoginForm()
    else:
        form=LoginForm(request.POST)
        if form.is_valid():
            
            password=request.POST.get('password')
            username=request.POST.get('username')
            
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request=request,user=user)
                message=f'Hello {user.username}, You have logged in'
            else:
                message='You fieled'
        
    context={'form':form}
    return render(request=request,template_name='register/login.html',context=context)