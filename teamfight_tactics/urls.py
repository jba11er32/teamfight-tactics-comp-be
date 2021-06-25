from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('comps/', views.CompList.as_view(), name='comp_list'),
    path('comps/<int:pk>', views.CompDetail.as_view(), name='comp_detail'),
]