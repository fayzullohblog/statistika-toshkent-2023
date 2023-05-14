from .models import ImageFile



def notview_pdfs(request):
    count_pdf=ImageFile.objects.filter(state=False).count()
    if count_pdf:
        return {'count_pdf':count_pdf}
    else:
        return {'count_pdf':0}
    
