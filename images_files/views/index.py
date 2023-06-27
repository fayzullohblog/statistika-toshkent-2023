from django.shortcuts import redirect, render
from common.alert import tg_alert
from common.choose import UserChoices
from django.core.paginator import Paginator
from ..models import ImageFile
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from ..serializer import ImageFileSerializer
from django.http import HttpResponse
# ---------------------------
# Create your views here.
# 

class CreateGenericsApiView(CreateModelMixin,GenericAPIView):
    serializer_class=ImageFileSerializer
    queryset=ImageFile.objects.all()

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



def index_view(request):
    try:
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.user != UserChoices.OWNER:
            return redirect('staff_zip')
        try:
            pdfs=ImageFile.objects.all().order_by('-created_date')
            pdfs_count=list(range(1,pdfs.count()+1))
            paginator=Paginator(pdfs,3)
            page_number=request.GET.get('page')
            page_obj=paginator.get_page(page_number)
        except Exception as e:
            pdfs=None
            tg_alert.custom_alert(f"Not Found any queryset in ImageFile model:  {e}")

        context={
            'pdfs':pdfs,
            'page_obj':page_obj,
            }
        
        return render(request=request,template_name='index.html',context=context)
    except Exception as e:
        tg_alert.custom_alert(f"You didn't login from web-site: {e}")
        return render(request=request,template_name='index.html',context=context)

