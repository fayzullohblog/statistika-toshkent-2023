from django.shortcuts import redirect
from common.choose import UserChoices
from ..models import ZipimagePart
from django.shortcuts import render

def staff_zip(request):
    if request.user.is_authenticated:
        if  request.user.user == UserChoices.STAFF:
            zips=ZipimagePart.objects.all()
            return render(request=request,template_name='staff_zip.html',context={'zips':zips})
        else:
            return redirect('index')
    else:
        return redirect('login')
