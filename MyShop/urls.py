from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductView.as_view()),
    path("<slug:slug>/", views.Product_detail.as_view(), name="product_detail")
]
