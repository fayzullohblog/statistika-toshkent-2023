from django.urls import path
from .views.index import index_view,CreateGenericsApiView
from .views.pdf_cut import PdfCutDjangoViews
from .views.staff_zip import staff_zip
from .views.page_delete import page_delete_view
from .views.create_zip import create_zip_view



urlpatterns = [
    path('index/',index_view,name='index'),
    path('pdf_cut/',PdfCutDjangoViews.as_view(),name='pdf_cut'),
    path('staff_zip/',staff_zip,name='staff_zip'),
    path('page_delete/',page_delete_view,name='page_delete'),
    path('pdf_cut/create_zip/',create_zip_view,name='create_zip'),
    path('createimagefile/',CreateGenericsApiView.as_view(),name='creategenericapiview'),
]