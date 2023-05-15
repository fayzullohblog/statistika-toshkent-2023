import qrcode
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen.canvas import Canvas

from config.settings import MEDIA_ROOT

class PdfParser:
    """
        Set pdf file path qrcode image into pdf file
    """
    def __init__(self, file, domain_name):
        self.file = MEDIA_ROOT / file
        self.domain_name = domain_name
        self.reader = PdfReader(self.file)

    def page_spliter(self):
        """
            Split pdf file into page 
        """
        yield from range(len(self.reader.pages))

    def create_pdf(self, save_folder_path, page, **kwargs)->str:
        """
            Create pdf file with qrcode image
        """
        # Get the watermark file you just created

        SAVED_FILE_PATH = save_folder_path / f"{page}.pdf"
        new_folder_name = str(save_folder_path).split('/')[-1]
        SAVED_FILE_PATH_FOR_QRCODE = f"{self.domain_name}/media/{new_folder_name}/{page}.pdf"
        SAVED_FILE_PATH_FOR_MODEL = f"{new_folder_name}/{page}.pdf"

        writer = PdfWriter()
        
        with open(SAVED_FILE_PATH, "wb") as file:
            qr_code_image = self.create_qrcode_image(SAVED_FILE_PATH_FOR_QRCODE)
            watermark_file = self.create_qrcode_pdf(qr_code_image=qr_code_image, **kwargs)
            watermark = PdfReader(open(watermark_file, "rb"))
            self.reader.pages[page].merge_page(watermark.pages[0]) # merge qrcode pdf file to pdf file
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


    def create_qrcode_pdf(self,  qr_code_image, watermark_file:str='watermark.pdf', **kwargs):
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
        if kwargs:
            #data
            data_1 = kwargs.get('data_1', '')
            data_2 = kwargs.get('data_2', '')
            #coordinates
            x_path_1 = kwargs.get('x_path_1', 0)
            y_path_1 = kwargs.get('y_path_1', 0)

            x_path_2 = kwargs.get('x_path_2', 0)
            y_path_2 = kwargs.get('y_path_2', 0)
            #draw data
            doc.drawString(x_path_1, y_path_1, data_1)
            doc.drawString(x_path_2, y_path_2, data_2)
            #TODO: add more data to pdf file
        doc.save()
        return watermark_file
