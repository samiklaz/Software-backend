from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('<str:slug>/', DictionaryAPIView.as_view()),
]