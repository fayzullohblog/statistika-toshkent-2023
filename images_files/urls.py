from django.urls import path
from .views.index import index
from .views.pdf_cut import PdfCutDjangoViews


urlpatterns = [
    path('',index,name='index'),
    path('pdf_cut/',PdfCutDjangoViews.as_view(),name='pdf_cut')
]