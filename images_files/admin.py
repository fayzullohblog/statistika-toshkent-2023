from django.contrib import admin
from .models import ImageFile,ImagePart,ZipimagePart
# Register your models here.
admin.site.register([ImageFile,ImagePart,ZipimagePart])
