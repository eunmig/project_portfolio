from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('save-deposit-products/', views.save_DP),
    path('deposit-products/', views.deposit_products),
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_PO),
    path('deposit-products/top_rate/', views.top_rate),
]
