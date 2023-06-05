from rest_framework.serializers import ModelSerializer
from .models import ImageFile

class ImageFileSerializer(ModelSerializer):
    class Meta:
        model=ImageFile
        fields=['image_pdf','name']
   