from django.shortcuts import redirect
from common.choose import UserChoices
from ..models import ZipimagePart
from django.shortcuts import render
from django.core.paginator import Paginator
from common.alert import tg_alert


def staff_zip(request):
    
    try:

        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.user != UserChoices.STAFF:
            return redirect('index')
        try:
            zips=ZipimagePart.objects.all().order_by('-created_date')
            paginator=Paginator(zips,3)
            page_number=request.GET.get('page')
            page_obj=paginator.get_page(page_number)
            return render(
                request=request,template_name='staff_zip.html',context={'page_obj':page_obj})
        except Exception as e:
            tg_alert.custom_alert(f"Don't found any zip file in ZipImagePart model: {e}")
    except Exception as e:
        tg_alert.custom_alert(f"You didn't login from web-site: {e}")

