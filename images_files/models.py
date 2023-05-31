from django.db import models
from account.models import Account
from common.models import BaseModel
# Create your models here.
class ImageFile(BaseModel):
       image_pdf=models.FileField(upload_to='images_pdf',unique=True)
       name=models.CharField(max_length=50,null=True,blank=True)
       state=models.BooleanField(default=False)
       def __str__(self):
              return  self.image_pdf.name
       class Meta:
              verbose_name='ImageFile'
              verbose_name_plural='ImageFiles'

       @property
       def pdfs_state(self):
              if self.state:
                     return 'Junatilgan'
              else:
                     return "Junatilmagan"
       
              
       @property
       def pdfs_name(self):
              if self.name:
                     return self.name
              else:
                     return "Name berilmadi"
              
       
              

class ImagePart(models.Model):
       imagefile=models.ForeignKey(ImageFile,related_name='imageparts', on_delete=models.CASCADE,null=True)
       oneimage=models.FileField(upload_to='oneimage')
       title=models.CharField(max_length=250,null=True,blank=True)
       created_date=models.DateTimeField(auto_now_add=True)
       updated_date=models.DateTimeField(auto_now=True)

    
       def __str__(self):
              return f'{self.title}'

       class Meta:
              verbose_name='ImagePart'
              verbose_name_plural='ImageParts'

class ZipimagePart(models.Model):
       zipfile=models.FileField()
       state=models.BooleanField(default=False)
       created_date=models.DateTimeField(auto_now_add=True)
       updated_date=models.DateTimeField(auto_now=True)

       def __str__(self):
              return self.zipfile.name
       
       
              





    