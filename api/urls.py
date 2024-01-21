from django.contrib import admin
from django.urls import path, include
from . import views
from .views import CmpApi

urlpatterns = [
    path('cmp/', views.compemp),
    path('cmp/<int:id>', views.compempgetone),
    path('cmp-api/<int:k>/', CmpApi.as_view(), name = 'cmp-api'),
    path('cmp-api/', CmpApi.as_view(), name = 'cmp-api')
]