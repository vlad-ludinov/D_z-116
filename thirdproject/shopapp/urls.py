from django.urls import path
from . import views


urlpatterns = [
    path("client/<int:client_id>", views.client, name="client"),
    path("client/<int:client_id>/<str:filter>", views.products, name="products")
]