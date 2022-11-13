from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='dashboard'),
    path('diagnose',skinCancer),
    path('social',social_help),
    path('sentimentAnalysis',sentimentAnalysis),
    path('donateData',donateData)
]