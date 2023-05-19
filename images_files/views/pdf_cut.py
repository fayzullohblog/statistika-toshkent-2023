from django.shortcuts import redirect
from common.choose import UserChoices
import os,zipfile,shutil
from django.shortcuts import get_object_or_404, render
from django.views import View
import random

from config.settings import MEDIA_ROOT

from ..models import ImageFile, ImagePart,ZipimagePart

from common.pdf_parser import PdfParser

class PdfCutDjangoViews(View):

    def get(self,request):
        if not request.user.is_authenticated:
            return redirect('login')
        if request.user.user != UserChoices.OWNER:
            return redirect('staff_zip')

        #TODO must check user is authenticated and user is admin or DIREKTOR becuase this page only for admin and direktor for security
        domain_name=request.META['HTTP_HOST']
        pdf_id=request.GET.get('pdf_id')
        print(request.user.degree)

        pdf_file_instance = get_object_or_404(ImageFile, pk=pdf_id)
        imagefile=pdf_file_instance.image_pdf.path

        new_folder_name=str(pdf_file_instance.image_pdf).split('/')[1]

        new_folder = MEDIA_ROOT / new_folder_name

        if os.path.exists(new_folder):
            shutil.rmtree(new_folder)
        os.makedirs(new_folder)

        pdf_file = PdfParser(imagefile, domain_name)
        pdf_file_instance.state=True
        pdf_file_instance.save(update_fields=['name'])

        for page in pdf_file.page_spliter():
            saved_page = pdf_file.create_pdf(save_folder_path=new_folder, page=page, 
                                            data_1=str(request.user.first_name), x_path_1=410, y_path_1=150,
                                            data_2=str(request.user.degree), x_path_2=100, y_path_2=150)
            ImagePart.objects.create(imagefile=pdf_file_instance, oneimage=saved_page, title=f"{page+1}-page")

        #create zip file
        split_imagefile=str(pdf_file_instance).split('/')[1]

        zip_filename=MEDIA_ROOT/f'{split_imagefile}.zip'

        pdf_files=[f for f in os.listdir(MEDIA_ROOT/split_imagefile) if f.endswith('.pdf')]

        with zipfile.ZipFile(zip_filename,'w',zipfile.ZIP_DEFLATED) as zip:
            for file_name in pdf_files:
                file_path=os.path.join(MEDIA_ROOT/split_imagefile,file_name)
                zip.write(file_path,file_name)

        #save zip file to database
        ZipimagePart.objects.create(zipfile=f'{new_folder_name}.zip')

        target_directory=MEDIA_ROOT
        shutil.move(zip_filename,os.path.join(target_directory,os.path.join(zip_filename)))

        zipimagepart=ZipimagePart.objects.all()

        return render(request=request,template_name='pdf_cut.html',context={'zipimagepart':zipimagepart})


        
        
