from django.urls import path
from . import views


urlpatterns = [
    path("client/<int:client_id>/products", views.client, name="client"),
    path("client/<int:client_id>/products/<str:filter>", views.products, name="products")
]