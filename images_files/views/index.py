from django.shortcuts import render
from ..models import ImageFile
# ---------------------------
# Create your views here.    
def index(request):
    pdfs=ImageFile.objects.all().order_by('-created_date')

    context={'pdfs':pdfs}
    return render(
    request=request,
    template_name='index.html',
    context=context)

