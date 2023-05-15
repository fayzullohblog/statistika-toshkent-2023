from django.shortcuts import redirect, render

from common.choose import UserChoices

from ..models import ImageFile


# ---------------------------
# Create your views here.    
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.user != UserChoices.OWNER:
        return redirect('staff_zip')
    try:
        pdfs=ImageFile.objects.all().order_by('-created_date')
    except Exception:
        pdfs=None

    context={
        'pdfs':pdfs,
            }
    return render(
    request=request,
    template_name='index.html',
    context=context)

