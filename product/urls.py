from django.contrib import admin
from django.urls import path
from product import views

urlpatterns = [
    path('' , views.ProductView.as_view()),
    path('<int:product_id>/' , views.ProductView.as_view()),
]
