from django.shortcuts import redirect
from common.choose import UserChoices
import os,zipfile,shutil
from django.shortcuts import get_object_or_404, render
from django.views import View
from config.settings import MEDIA_ROOT
from ..models import ImageFile, ImagePart,ZipimagePart
from common.pdf_parser import PdfParser
from django.http import HttpResponse

from reportlab.pdfgen import canvas
from reportlab.lib import styles

class PdfCutDjangoViews(View):

    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.user != UserChoices.OWNER:
            return redirect('staff_zip')
        if request.user.degree is  None  and request.user.first_name is None:
            return HttpResponse(f'Sizning  <b style="color:red;">Ism</b> va <b  style="color:red;">Darajangiz </b> admin panelga kirgizilmadi !!!! <br> <a href="http://64.226.66.478000/admin/">Admin Panelga o\'tish</a> ')

        #TODO must check user is authenticated and user is admin or DIREKTOR becuase this page only for admin and direktor for security
        domain_name=request.META['HTTP_HOST']
        pdf_id=request.GET.get('pdf_id')
        
        pdf_file_instance = get_object_or_404(ImageFile, pk=pdf_id)

        imagefile=pdf_file_instance.image_pdf.path

        new_folder_name=str(pdf_file_instance.image_pdf).split('/')[1]
        new_folder = MEDIA_ROOT / new_folder_name
       
        if new_folder.exists() != True:
            #if folder name must be unique
            new_folder.mkdir()
            
            pdf_file = PdfParser(imagefile, domain_name)
            pdf_file_instance.state=True
            pdf_file_instance.save(update_fields=['name'])
            import html
            
            for page in pdf_file.page_spliter():
                saved_page = pdf_file.create_pdf(
                                                save_folder_path=new_folder,
                                                page=page, 
                                                # new_folder_name=new_folder_name,
                                                data_1=request.user.first_name, 
                                                x_path_1=420, y_path_1=130,

                                                data_2=request.user.degree,
                                                x_path_2=80, y_path_2=130
                                                )
                saved_file_path_qrcode = f'{new_folder_name}/{page}.pdf'
                
                ImagePart.objects.create(imagefile=pdf_file_instance, oneimage=saved_file_path_qrcode, title=f"{page+1}-page")
            return render(request=request,template_name='pdf_cut.html')

        image_file=ImageFile.objects.filter(state=True).all()
        imagepart=pdf_file_instance.imageparts.all()
        context={

                'image_file':image_file,
                'imagepart':imagepart,
                'pdf_id':pdf_id
        }

        return render(request=request,template_name='pdf_cut.html',context=context)



