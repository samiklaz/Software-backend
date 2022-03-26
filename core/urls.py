from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('<str:slug>/', CovidAPIView.as_view(), name='covid_api'),
]