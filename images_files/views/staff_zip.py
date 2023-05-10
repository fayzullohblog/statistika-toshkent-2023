from ..models import ZipimagePart
from django.shortcuts import render

def staff_zip(request):
    zips=ZipimagePart.objects.all()  #.order_by('-created_date')
    print('-----zip',request.POST.get('zip_id'))

    return render(request=request,template_name='staff_zip.html',context={'zips':zips})