from common.choose import UserChoices
from django.shortcuts import redirect
from django.shortcuts import render
from ..models import ImageFile
# ---------------------------
# Create your views here.    
def index(request):
    if request.user.is_authenticated:
        if request.user.user == UserChoices.OWNER:
            try:
                pdfs=ImageFile.objects.all().order_by('-created_date')
            except:
                
                pdfs=None

            context={
                'pdfs':pdfs,
                    }
            return render(
            request=request,
            template_name='index.html',
            context=context)
        else:
            return redirect('staff_zip')
    else:
        return redirect('login')

