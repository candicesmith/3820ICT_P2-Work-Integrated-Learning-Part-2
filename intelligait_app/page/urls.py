from django.urls import path
from django.conf.urls import url
from .views import (
    ClientListView, ClientDetailView, ClientCreateView, 
    ClientUpdateView, ClientDeleteView, ClientAnalysisView, ClientUploadView, 
    ClientVideosView
)
from . import views

urlpatterns = [
    path('', ClientListView.as_view(), name='page-home'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='client'),
    path('client/<int:pk>/analysis', ClientAnalysisView.as_view(), name='client-analysis'),
    path('client/<int:pk>/videos', ClientVideosView.as_view(), name='client-videos'),
    path('create-client/', ClientCreateView.as_view(), name='create-client'),
    path('client/<int:pk>/update', ClientUpdateView.as_view(), name='update-client'),
    path('client/<int:pk>/delete', ClientDeleteView.as_view(), name='delete-client'),
    path('client/<int:pk>/upload-video/', ClientUploadView.as_view(), name='upload-video'),
    url(r'view-pdf/$', views.pdf_view, name='pdf-view'),
]
