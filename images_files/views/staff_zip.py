from django.shortcuts import redirect
from common.choose import UserChoices
from ..models import ZipimagePart
from django.shortcuts import render

def staff_zip(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.user != UserChoices.STAFF:
        return redirect('index')
    zips=ZipimagePart.objects.all()
    return render(request=request,template_name='staff_zip.html',context={'zips':zips})
