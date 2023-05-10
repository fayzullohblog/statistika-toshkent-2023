from django.urls import path
from .views.index import index
from .views.pdf_cut import PdfCutDjangoViews
from .views.staff_zip import staff_zip


urlpatterns = [
    path('index/',index,name='index'),
    path('pdf_cut/',PdfCutDjangoViews.as_view(),name='pdf_cut'),
    path('staff_zip/',staff_zip,name='staff_zip')
    

]