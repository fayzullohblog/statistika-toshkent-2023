from django.shortcuts import redirect
from ..models import ImagePart,ImageFile


def page_delete_view(request):
    pdf_id=request.GET.get('pdf_id')
    page_id=request.GET.get('page_id')
    url = f'/pdf_cut/?pdf_id={pdf_id}'
    
    # if request.method=='POST':

    imagefile=ImageFile.objects.get(id=pdf_id)
    imagepart=ImagePart.objects.get(imagefile=imagefile,id=page_id).delete()
    
    return redirect(url)

    