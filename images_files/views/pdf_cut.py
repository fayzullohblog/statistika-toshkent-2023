import os,zipfile,shutil
import qrcode
from django.shortcuts import get_object_or_404, render
from django.views import View
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen.canvas import Canvas

from config.settings import MEDIA_ROOT

from ..models import ImageFile, ImagePart,ZipimagePart


class PdfCutDjangoViews(View):

    def get(self,request):
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
            class PdfParser:
                """
                    Set pdf file path qrcode image into pdf file
                """
                def __init__(self, file):
                    self.file = MEDIA_ROOT / file
                    self.reader = PdfReader(self.file)

                def page_spliter(self):
                    """
                        Split pdf file into page 
                    """
                    yield from range(len(self.reader.pages))

                def create_pdf(self, save_folder_path, page)->str:
                    """
                        Create pdf file with qrcode image
                    """
                    # Get the watermark file you just created

                    SAVED_FILE_PATH = save_folder_path / f"{page}.pdf"
                    #/home/ubuntu/statistika/media/Tavba_kitobi.pdf/54.pdf get only Tavba_kitobi.pdf/54.pdf
                    new_folder_name = str(save_folder_path).split('/')[-1]
                    SAVED_FILE_PATH_FOR_QRCODE = f"{domain_name}/media/{new_folder_name}/{page}.pdf"
                    SAVED_FILE_PATH_FOR_MODEL = f"{new_folder_name}/{page}.pdf"

                    writer = PdfWriter()
                    
                    with open(SAVED_FILE_PATH, "wb") as file:
                        # create qrcode image
                        qr_code_image = self.create_qrcode_image(SAVED_FILE_PATH_FOR_QRCODE)
                        # create qrcode pdf file
                        watermark_file = self.create_qrcode_pdf(qr_code_image=qr_code_image)
                        watermark = PdfReader(open(watermark_file, "rb"))
                        # print('--water',watermark.getPage())
                        self.reader.pages[page].merge_page(watermark.pages[0]) # merge qrcode pdf file to pdf file
                        # add qrcode image to pdf file
                        writer.add_page(self.reader.pages[page]) # add page to pdf file
                        writer.write(file) # write pdf file
                        
                    
                    return SAVED_FILE_PATH_FOR_MODEL
                        
                def create_qrcode_image(self, save_folder_path):
                    qr_code = qrcode.QRCode(
                        version=1,
                        error_correction=qrcode.constants.ERROR_CORRECT_L,
                        box_size=3,
                        border=3,
                    )
                    qr_code.add_data(save_folder_path)
                    qr_code.make(fit=True)
                    qr_code_image = qr_code.make_image(fill_color="black", back_color="white")
                    qr_code_image.save(MEDIA_ROOT / "data.png")
                    return MEDIA_ROOT / "data.png"


                def create_qrcode_pdf(self,  qr_code_image, watermark_file:str='watermark.pdf'):
                    """
                        Create pdf file with qrcode image
                    """
                    # if watermark_file doesn't exist, create it
                    watermark_file = MEDIA_ROOT / watermark_file
                    if not watermark_file.exists():
                        watermark_file.touch()

                    doc = Canvas(str(MEDIA_ROOT / watermark_file))
                    # draw the QR code at the specified coordinates
                    doc.drawImage(qr_code_image, 295, 95)
                    doc.save()
                    return watermark_file
                
            pdf_file = PdfParser(imagefile)
            pdf_file_instance.state=True
            pdf_file_instance.save(update_fields=['name'])

            for page in pdf_file.page_spliter():
                saved_page = pdf_file.create_pdf(save_folder_path=new_folder, page=page)
                ImagePart.objects.create(imagefile=pdf_file_instance, oneimage=saved_page, title=f"{page+1}-page")
             
            split_imagefile=str(pdf_file_instance).split('/')[1]
        
            zip_filename=MEDIA_ROOT/f'{split_imagefile}.zip'

            pdf_files=[f for f in os.listdir(MEDIA_ROOT/split_imagefile) if f.endswith('.pdf')]

            with zipfile.ZipFile(zip_filename,'w',zipfile.ZIP_DEFLATED) as zip:
                for file_name in pdf_files:
                    file_path=os.path.join(MEDIA_ROOT/split_imagefile,file_name)
                    zip.write(file_path,file_name)

            ZipimagePart.objects.create(zipfile=f'{new_folder_name}.zip')


            target_directory=MEDIA_ROOT
            shutil.move(zip_filename,os.path.join(target_directory,os.path.join(zip_filename)))
           
            zipimagepart=ZipimagePart.objects.all()
            

            return render(request=request,template_name='pdf_cut.html',context={'zipimagepart':zipimagepart})
    
        pdf_file_instance.state=True
        pdf_file_instance.save(update_fields=['state'])
        
        image_file=ImageFile.objects.filter(state=True).all()


        imagepart=pdf_file_instance.imageparts.all()
    
        


        context={
                
                'image_file':image_file,
                'imagepart':imagepart
        }
        
        return render(request=request,template_name='pdf_cut.html',context=context)
 
 
