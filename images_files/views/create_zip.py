from django.shortcuts import render,redirect
from config.settings import MEDIA_ROOT
import os,zipfile,shutil
from ..models import ZipimagePart,ImageFile
from django.shortcuts import get_object_or_404



def create_zip_view(request):
    

    if request.method=='POST':
        pdf_id=request.POST.get('pdf_id')
        pdf_file_instance = get_object_or_404(ImageFile, pk=pdf_id)
        new_folder_name=str(pdf_file_instance.image_pdf).split('/')[1]
        url = f'/pdf_cut/?pdf_id={pdf_id}'

       


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

        pdf_file_instance.state=True
        pdf_file_instance.save(update_fields=['state'])

        return redirect(url)
