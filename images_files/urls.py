from django.urls import path
from .views.index import index
from .views.pdf_cut import PdfCutDjangoViews,get_pdf_cut


urlpatterns = [
    path('',index,name='index'),
    path('pdf_cut/',PdfCutDjangoViews.as_view(),name='pdf_cut'),
    path('get_pdf_cut/',get_pdf_cut,name='get_pdf_cut')

]